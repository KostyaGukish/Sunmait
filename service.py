from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
pipe = pipeline("summarization", model="IlyaGusev/rut5_base_sum_gazeta")


class TextInput(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    prediction: dict


@app.get("/ping")
async def ping():
    return {"status": "OK"}


@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: TextInput):
    result = pipe(input_data.text)
    return PredictionOutput(prediction=result[0])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
