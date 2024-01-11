from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import app.prediction as prediction 

app = FastAPI()

class PostValues(BaseModel):
    value: dict

class PredictInput(BaseModel):
    data: dict

class PredictOutput(BaseModel):
    predict: dict

@app.get("/")
async def read_root():
    return "Welcome to, Bank Marketing App API!"

@app.post("/postValues", response_model=PostValues)
async def post_values(value: dict):
    if value:
        return {"value": value}
    raise HTTPException(status_code=400, detail="Invalid format.")

@app.post("/getPredictionOutput", response_model=PredictOutput)
async def get_prediction_output(input_data: PredictInput):
    try:
        predict_output = prediction.predict_mpg(input_data.data)
        res = {"value": predict_output}
        return {'predict': res}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
