import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Load trained model, encoder, and scalers
theta_final = joblib.load("best_model.pkl")  
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")
encoder = joblib.load("country_encoder.pkl")

print("Model, encoder, and scalers loaded successfully!")

# Initialize FastAPI app
app = FastAPI()

# CORS setup
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionInput(BaseModel):
    rating: float = Field(..., ge=1.0, le=10.0, description="Rating must be between 1 and 10")
    revenue: float = Field(..., gt=0, description="Revenue must be a positive number")
    country: str = Field(..., min_length=1, description="Country cannot be empty")

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Create input DataFrame
        df_input = pd.DataFrame([input_data.dict()])

        # Rename columns for consistency
        df_input.rename(columns={
            "rating": "Rating",
            "revenue": "Revenue",
            "country": "Country"
        }, inplace=True)

        # Log-transform revenue
        df_input["Revenue"] = np.log1p(df_input["Revenue"])

        # One-hot encode the country
        encoded_country = encoder.transform([[df_input["Country"].values[0]]])
        encoded_country_df = pd.DataFrame(encoded_country, columns=encoder.get_feature_names_out(["Country"]))

        # Drop the original 'Country' column and add encoded country features
        df_input = df_input.drop(columns=["Country"])
        df_input = pd.concat([df_input, encoded_country_df], axis=1)

        # Standardize the input features
        input_scaled = scaler_X.transform(df_input)

        # Make prediction using the trained model
        y_pred_std = theta_final.predict(input_scaled).item()

        # Inverse transform and get the predicted visitors
        log_prediction = scaler_y.inverse_transform([[y_pred_std]])[0][0]
        prediction_original = np.expm1(log_prediction)

        return {"predicted_visitors": round(prediction_original)}

    except Exception as e:
        return {"error": str(e)}
