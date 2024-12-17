import torch
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Import your trained model
from model import SimpleModel

# Initialize the FastAPI app
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = SimpleModel()
checkpoint = torch.load("checkpoint.pth", weights_only=True)
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()  # Set the model to evaluation mode


# Define the input schema using Pydantic
class PredictionRequest(BaseModel):
    inputs: List[List[float]]  # A list of samples, each sample is a list of floats


# Define the output schema
class PredictionResponse(BaseModel):
    predictions: List[float]


# Define the prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        # Convert the input data to a PyTorch tensor
        inputs_tensor = torch.tensor(request.inputs, dtype=torch.float32)

        # Perform inference
        with torch.no_grad():
            outputs = model(inputs_tensor)

        # Extract predictions and convert them to a list
        if outputs.size(1) == 1:
            predictions = outputs.squeeze(1).tolist()

        # Return predictions
        return PredictionResponse(predictions=predictions)
    except Exception as e:
        return {"error": str(e)}


# Health check endpoint
@app.get("/")
def health_check():
    return {"message": "Model API is running!"}
