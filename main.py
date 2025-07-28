from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

# Define request body format
class VoiceFeatures(BaseModel):
    features: list[float]

# Load model
model = None
model_path = "gender_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✅ Model loaded successfully.")
else:
    print("❌ Model file not found!")

@app.post("/predict")
def predict(data: VoiceFeatures):
    if model is None:
        return {"error": "Model not loaded."}
    try:
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        return {"gender": "male" if prediction == 1 else "female"}
    except Exception as e:
        return {"error": str(e)}
