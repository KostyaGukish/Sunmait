from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sklearn
import numpy as np
from typing import List
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="ML Prediction Server",
             description="A simple API for health checks and random predictions",
             version="1.0.0")

# Data model for prediction input
class PredictionInput(BaseModel):
    features: List[float]

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Check if the server is running and accessible
    Returns:
        dict: Status message and sklearn version
    """
    return {
        "status": "healthy",
        "sklearn_version": sklearn.__version__
    }

# Prediction endpoint
@app.post("/predict")
async def predict(data: PredictionInput):
    """
    Generate a random prediction based on input data
    Args:
        data: Input features for prediction
    Returns:
        dict: Random prediction result
    """
    try:
        # Validate input
        if not data.features or len(data.features) == 0:
            raise HTTPException(status_code=400, detail="Input features cannot be empty")
        
        # Generate random prediction (0 or 1)
        prediction = np.random.randint(0, 2)
        
        return {
            "prediction": int(prediction),
            "input_features": data.features,
            "confidence": float(np.random.random())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Hello world endpoint
@app.get("/hello")
async def hello_world():
    """
    Simple hello world endpoint
    Returns:
        dict: Greeting message
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
