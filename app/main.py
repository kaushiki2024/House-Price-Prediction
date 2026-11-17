
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained ML model
model = joblib.load("house_price_model.pkl")


# Define input features using Pydantic
class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


# Home endpoint
@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}


# Prediction endpoint
@app.post("/predict")
def predict_price(data: HouseData):

    input_data = [[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]]

    prediction = model.predict(input_data)

    predicted_price = prediction[0] * 100000

    return {
        "predicted_price": round(float(predicted_price), 2)
    }
