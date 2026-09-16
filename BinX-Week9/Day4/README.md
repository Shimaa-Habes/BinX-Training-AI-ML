<div style="background: linear-gradient(135deg, #F0FAF7 0%, #E0F5EC 50%, #D4F0E3 100%); border: 2px solid #5FB49C; border-radius:20px; padding:30px; box-sizing:border-box; overflow:hidden;">

<div style="display:flex; justify-content:center; align-items:center; gap:10px; margin-bottom:15px; flex-wrap:wrap;">
<span style="background:#FFFFFF; color:#2E8B7A; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:bold; border:1px solid #5FB49C;">
🌿 Week 9 · Sprint 4
</span>
<span style="background:#FFFFFF; color:#2E8B7A; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:bold; border:1px solid #5FB49C;">
✅ Day 4
</span>
</div>

<h1 style="color:#1F7A66; font-size:32px; margin:0; text-align:center; font-weight:bold;">
🚀 Public Deployment
</h1>

<p style="color:#3D6B5C; font-size:16px; text-align:center; margin-top:10px; font-weight:bold;">
Taking the model from my laptop to a public URL the whole world can open 🌍
</p>

<div style="display:flex; gap:10px; margin-top:20px; flex-wrap:wrap; justify-content:center;">
<div style="background:#FFFFFF; padding:10px 16px; border-radius:14px; border:1px solid #9DD9C4; color:#1F7A66; font-size:13px; font-weight:bold;">
🤗 Hugging Face Spaces
</div>
<div style="background:#FFFFFF; padding:10px 16px; border-radius:14px; border:1px solid #9DD9C4; color:#1F7A66; font-size:13px; font-weight:bold;">
📦 requirements.txt
</div>
<div style="background:#FFFFFF; padding:10px 16px; border-radius:14px; border:1px solid #9DD9C4; color:#1F7A66; font-size:13px; font-weight:bold;">
🧪 Live Testing
</div>
</div>

</div>

---

<div style="background: #F0FAF7; border-left:5px solid #5FB49C; padding:18px 22px; border-radius:14px; width:100%; box-sizing:border-box; margin-top:10px;">
<h2 style="color:#1F7A66; font-size:22px; margin:0; font-weight:bold;">
📝 Overview
</h2>
<p style="color:#3D6B5C; font-size:16px; line-height:1.7; margin-top:10px; font-weight:bold;">
Today's focus was on taking a trained model from a local notebook to a
live, publicly accessible application — choosing a hosting platform,
preparing a correct requirements.txt, handling model and preprocessing
files correctly, and testing a live deployment against local results.
</p>
</div>

---

<div style="background: #F0FAF7; border-left:5px solid #5FB49C; padding:18px 22px; border-radius:14px; width:100%; box-sizing:border-box;">
<h2 style="color:#1F7A66; font-size:22px; margin:0; font-weight:bold;">
📚 What I Learned
</h2>
</div>

<div style="background:#FFFFFF; border:1px solid #9DD9C4; border-radius:14px; padding:16px 20px; margin-top:10px; box-sizing:border-box;">
<h3 style="color:#2E8B7A; font-size:18px; margin:0; font-weight:bold;">🌍 4.1 From Local to Public</h3>
<p style="color:#3D6B5C; font-size:15px; line-height:1.7; margin-top:8px;">
Compared free hosting platforms — Hugging Face Spaces, Render, and
Railway — and when each is the better fit. Hugging Face Spaces is
usually the fastest route for a Streamlit demo, since it builds and
hosts automatically from a pushed repository.
</p>
</div>

<div style="background:#FFFFFF; border:1px solid #9DD9C4; border-radius:14px; padding:16px 20px; margin-top:10px; box-sizing:border-box;">
<h3 style="color:#2E8B7A; font-size:18px; margin:0; font-weight:bold;">📦 4.2 The requirements.txt Is Critical</h3>
<p style="color:#3D6B5C; font-size:15px; line-height:1.7; margin-top:8px;">
Created a correctly pinned requirements.txt with exact library versions
(streamlit, scikit-learn, joblib, numpy, pandas). A missing or
mismatched version can silently break the deployment build.
</p>
</div>

<div style="background:#FFFFFF; border:1px solid #9DD9C4; border-radius:14px; padding:16px 20px; margin-top:10px; box-sizing:border-box;">
<h3 style="color:#2E8B7A; font-size:18px; margin:0; font-weight:bold;">📁 4.3 Handling Model Files</h3>
<p style="color:#3D6B5C; font-size:15px; line-height:1.7; margin-top:8px;">
Learned that serialized model and preprocessing files must be included
in the deployment repo (or downloaded at startup for large models), and
that file paths must be relative and verified to work in the hosting
environment. Guiding principle: deploy early and iterate — a
live-but-simple app beats a polished-but-local one.
</p>
</div>

<div style="background:#FFFFFF; border:1px solid #9DD9C4; border-radius:14px; padding:16px 20px; margin-top:10px; box-sizing:border-box;">
<h3 style="color:#2E8B7A; font-size:18px; margin:0; font-weight:bold;">🧪 4.4 Testing the Live Deployment</h3>
<p style="color:#3D6B5C; font-size:15px; line-height:1.7; margin-top:8px;">
Learned to test a live deployment the way a real user would, including
edge cases, and to trace any mismatch between local and deployed
predictions back to preprocessing or dependency differences.
</p>
</div>

---

<div style="background: linear-gradient(135deg, #F0FAF7 0%, #E0F5EC 100%); border: 2px solid #5FB49C; border-radius:16px; padding:24px; width:100%; box-sizing:border-box; margin-top:10px;">
<h2 style="color:#1F7A66; font-size:24px; margin:0; text-align:center; font-weight:bold;">
🧪 Hands-On Lab: Going Live
</h2>
</div>

<table style="width:100%; border-collapse: collapse; margin-top:12px; border-radius:10px; overflow:hidden;">
<tr style="background-color:#5FB49C;">
<th style="border: 1px solid #9DD9C4; padding:10px; color:#FFFFFF; font-weight:bold;">#</th>
<th style="border: 1px solid #9DD9C4; padding:10px; color:#FFFFFF; font-weight:bold;">Task</th>
<th style="border: 1px solid #9DD9C4; padding:10px; color:#FFFFFF; font-weight:bold;">Status</th>
</tr>
<tr>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#1F7A66; background:#F0FAF7;">1</td>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#3D6B5C; background:#F0FAF7;">Choose a hosting platform and create the deployment repo/Space</td>
<td style="border: 1px solid #9DD9C4; padding:10px; background:#F0FAF7;">⏸️ Deferred</td>
</tr>
<tr>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#1F7A66; background:#FFFFFF;">2</td>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#3D6B5C; background:#FFFFFF;">Push the app, model, preprocessing files, and requirements.txt</td>
<td style="border: 1px solid #9DD9C4; padding:10px; background:#FFFFFF;">⏸️ Deferred</td>
</tr>
<tr>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#1F7A66; background:#F0FAF7;">3</td>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#3D6B5C; background:#F0FAF7;">Confirm the build succeeds and obtain the public URL</td>
<td style="border: 1px solid #9DD9C4; padding:10px; background:#F0FAF7;">⏸️ Deferred</td>
</tr>
<tr>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#1F7A66; background:#FFFFFF;">4</td>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#3D6B5C; background:#FFFFFF;">Test the live app and confirm predictions match the local version</td>
<td style="border: 1px solid #9DD9C4; padding:10px; background:#FFFFFF;">⏸️ Deferred</td>
</tr>
<tr>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#1F7A66; background:#F0FAF7;">5</td>
<td style="border: 1px solid #9DD9C4; padding:10px; color:#3D6B5C; background:#F0FAF7;">Record the public URL in the project README</td>
<td style="border: 1px solid #9DD9C4; padding:10px; background:#F0FAF7;">⏸️ Deferred</td>
</tr>
</table>

<div style="background-color:#FFF9F0; border-left:5px solid #F0D9B5; padding:16px 20px; border-radius:12px; margin-top:14px; box-sizing:border-box;">
<p style="color:#8B7355; font-size:14px; line-height:1.7; margin:0;">
📌 <b>Note:</b> While setting up the Space on Hugging Face, Streamlit was
no longer available as a direct SDK option — Streamlit apps are now
built using the Docker template, or via alternative SDKs like Gradio.
The actual live deployment step has been deferred to allow time to work
through this properly. The requirements.txt, model serialization, and
testing approach are fully prepared and ready to apply once deployment
resumes.
</p>
</div>

---

<div style="background: #F0FAF7; border-left:5px solid #5FB49C; padding:18px 22px; border-radius:14px; width:100%; box-sizing:border-box;">
<h2 style="color:#1F7A66; font-size:22px; margin:0; font-weight:bold;">
🧰 Tools Used
</h2>
<p style="color:#3D6B5C; font-size:16px; line-height:1.7; margin-top:10px; font-weight:bold;">
Streamlit · Hugging Face Spaces (attempted) · requirements.txt · Python
· requests (for live API testing) · Jupyter Notebook
</p>
</div>

---

<div style="background: linear-gradient(135deg, #F0FAF7 0%, #E0F5EC 100%); border: 2px solid #5FB49C; border-radius:16px; padding:22px; width:100%; box-sizing:border-box;">
<h2 style="color:#1F7A66; font-size:22px; margin:0; font-weight:bold;">
💡 Key Takeaway
</h2>
<p style="color:#3D6B5C; font-size:16px; line-height:1.7; margin-top:10px; font-weight:bold;">
A model in a notebook helps no one — deployment is what turns a trained
model into something real users can actually use. Even when a
platform's setup changes unexpectedly, the underlying steps (pin
dependencies, package model files correctly, test like a real user)
stay the same regardless of which host is eventually used.
</p>
</div>
