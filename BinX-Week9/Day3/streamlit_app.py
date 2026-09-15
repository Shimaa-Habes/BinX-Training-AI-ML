import streamlit as st
import joblib

model = joblib.load("BinX-Week9/Day1/model.joblib")
scaler = joblib.load("BinX-Week9/Day1/scaler.joblib")

st.title("Breast Cancer Prediction Dashboard")

st.write(
    "This dashboard uses a trained machine learning model to predict "
    "breast cancer classification from 30 numeric features."
)

st.subheader("Mean Features")

mean_radius = st.number_input("Mean Radius", min_value=0.0, max_value=50.0, value=14.13)
mean_texture = st.number_input("Mean Texture", min_value=0.0, max_value=50.0, value=19.29)
mean_perimeter = st.number_input("Mean Perimeter", min_value=0.0, max_value=200.0, value=91.97)
mean_area = st.number_input("Mean Area", min_value=0.0, max_value=3000.0, value=654.89)
mean_smoothness = st.number_input("Mean Smoothness", min_value=0.0, max_value=1.0, value=0.096)
mean_compactness = st.number_input("Mean Compactness", min_value=0.0, max_value=1.0, value=0.104)
mean_concavity = st.number_input("Mean Concavity", min_value=0.0, max_value=1.0, value=0.089)
mean_concave_points = st.number_input("Mean Concave Points", min_value=0.0, max_value=1.0, value=0.049)
mean_symmetry = st.number_input("Mean Symmetry", min_value=0.0, max_value=1.0, value=0.181)
mean_fractal_dimension = st.number_input("Mean Fractal Dimension", min_value=0.0, max_value=1.0, value=0.063)

st.subheader("Error Features")

radius_error = st.number_input("Radius Error", value=0.405)
texture_error = st.number_input("Texture Error", value=1.216)
perimeter_error = st.number_input("Perimeter Error", value=2.866)
area_error = st.number_input("Area Error", value=40.337)
smoothness_error = st.number_input("Smoothness Error", value=0.007)
compactness_error = st.number_input("Compactness Error", value=0.025)
concavity_error = st.number_input("Concavity Error", value=0.032)
concave_points_error = st.number_input("Concave Points Error", value=0.012)
symmetry_error = st.number_input("Symmetry Error", value=0.020)
fractal_dimension_error = st.number_input("Fractal Dimension Error", value=0.004)

st.subheader("Worst Features")

worst_radius = st.number_input("Worst Radius", value=16.27)
worst_texture = st.number_input("Worst Texture", value=25.68)
worst_perimeter = st.number_input("Worst Perimeter", value=107.26)
worst_area = st.number_input("Worst Area", value=880.58)
worst_smoothness = st.number_input("Worst Smoothness", value=0.132)
worst_compactness = st.number_input("Worst Compactness", value=0.254)
worst_concavity = st.number_input("Worst Concavity", value=0.272)
worst_concave_points = st.number_input("Worst Concave Points", value=0.115)
worst_symmetry = st.number_input("Worst Symmetry", value=0.290)
worst_fractal_dimension = st.number_input("Worst Fractal Dimension", value=0.084)

if st.button("Predict"):

    input_data = [[
        mean_radius,
        mean_texture,
        mean_perimeter,
        mean_area,
        mean_smoothness,
        mean_compactness,
        mean_concavity,
        mean_concave_points,
        mean_symmetry,
        mean_fractal_dimension,
        radius_error,
        texture_error,
        perimeter_error,
        area_error,
        smoothness_error,
        compactness_error,
        concavity_error,
        concave_points_error,
        symmetry_error,
        fractal_dimension_error,
        worst_radius,
        worst_texture,
        worst_perimeter,
        worst_area,
        worst_smoothness,
        worst_compactness,
        worst_concavity,
        worst_concave_points,
        worst_symmetry,
        worst_fractal_dimension
    ]]

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    prediction = int(prediction[0])
    probabilities = model.predict_proba(scaled_input)[0]

    if prediction == 0:
        st.error("Prediction: Malignant")
    else:
        st.success("Prediction: Benign")

    st.subheader("Prediction Probability")

malignant_probability = probabilities[0]
benign_probability = probabilities[1]

col1, col2 = st.columns(2)

with col1:
    st.metric("Malignant", f"{malignant_probability:.1%}")
    st.progress(float(malignant_probability))

with col2:
    st.metric("Benign", f"{benign_probability:.1%}")
    st.progress(float(benign_probability))
    
    st.caption("Educational demo only — this model is not a medical diagnosis.")