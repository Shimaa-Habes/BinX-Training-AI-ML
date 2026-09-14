# 🚀 Week 9 — Day 2: Serving the Model with FastAPI

<div style="
    width:100%;
    box-sizing:border-box;
    margin:18px 0 30px 0;
    padding:32px 38px;
    background:linear-gradient(135deg,#FBFAF7 0%,#F3F0E9 100%);
    border:1px solid #DDD8CC;
    border-radius:22px;
    box-shadow:0 8px 24px rgba(70,60,45,0.06);
">

## 🎯 Day 2 Overview

In this day, I built a **FastAPI prediction API** to serve the machine learning model saved during Day 1.

The API receives input data, validates it using **Pydantic**, applies the saved **StandardScaler**, sends the processed data to the saved model, and returns the prediction as a **JSON response**.

The API was tested locally through **Swagger UI** to verify predictions and input validation.

---

## ⚙️ Technologies Used

| Technology          | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| 🚀 **FastAPI**      | Build the REST API and create the prediction endpoint        |
| 🛡️ **Pydantic**     | Validate the incoming input data                             |
| ⚡ **Uvicorn**      | Run the FastAPI application locally                          |
| 💾 **Joblib**       | Load the saved model and scaler                              |
| 🧠 **Scikit-learn** | Provide the trained machine learning model and preprocessing |

---

## 🔌 Prediction Endpoint

### 📡 POST `/predict`

The `/predict` endpoint receives the **30 features** of the Breast Cancer dataset as JSON input.

The input is validated using the Pydantic `InputData` schema. After validation, the saved scaler transforms the input before it is passed to the saved model.

The prediction is returned as a JSON response.

```json
{
  "prediction": 0
}
```

---

## 🔄 Preprocessing Flow

The prediction pipeline follows this sequence:

**Client Input**
↓
**Pydantic Validation**
↓
**`scaler.joblib` — Transform Input**
↓
**`model.joblib` — Generate Prediction**
↓
**JSON Response**

The saved `scaler.joblib` is used before the model to keep preprocessing consistent with the training process from Day 1.

---

## 🧪 API Testing

The API was tested locally using **Swagger UI**.

**Swagger URL:** `http://127.0.0.1:8000/docs`

### 🔍 Testing Process

Opened **POST `/predict`**, clicked **Try it out**, entered valid JSON containing all 30 features, and clicked **Execute**.

The endpoint was tested with several different valid inputs.

### ✅ Testing Result

The requests were processed successfully and returned **HTTP 200 OK** responses with prediction results in JSON format.

Example:

```json
{
  "prediction": 0
}
```

---

## 🛡️ Invalid Input Validation

Invalid input was tested to confirm that Pydantic rejects incorrect requests.

Two validation cases were tested:

- A required field, `mean_radius`, was removed.
- An invalid string value was provided for `mean_texture`.

Pydantic rejected the invalid input and returned clear validation errors for both cases.

---

## 📋 Completion Checklist

- [x] 🚀 FastAPI application created
- [x] 📚 FastAPI, Pydantic, and Uvicorn documented
- [x] 🔌 `/predict` endpoint documented
- [x] 🔄 Preprocessing flow documented
- [x] 🧪 API tested through `/docs`
- [x] 🔢 Multiple valid inputs tested
- [x] 🛡️ Invalid input validation tested
- [x] 💾 Saved model and scaler verified
- [x] 📝 Testing results documented

---

## 🎉 Day 2 Result

Successfully built and tested a **FastAPI model-serving API** that validates input, applies the saved preprocessing pipeline, generates predictions, and returns them through a REST API.

</div>
