import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model, encoder, and scalers
theta_final = joblib.load("linear_regression_model.pkl")  
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")

print("Model, encoder, and scalers loaded successfully!")
# Initialize FastAPI app
app = FastAPI()

# CORS setup
origins = [
    "*",  # Example: Replace with your frontend's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)



class PredictionInput(BaseModel):
    rating: float
    revenue: float

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Create input DataFrame
        df_input = pd.DataFrame([input_data.dict()])

        # Rename columns for consistency with model's feature names
        df_input.rename(columns={
            "rating": "Rating",
            "revenue": "Revenue"
        }, inplace=True)

        # Log-transform revenue
        df_input['Revenue'] = np.log1p(df_input['Revenue'])
        
        # Standardize the input features
        input_scaled = scaler_X.transform(df_input)


        # Add bias term
        input_scaled = np.c_[np.ones((input_scaled.shape[0], 1)), input_scaled]

        # Make prediction
        y_pred_std = np.dot(input_scaled, theta_final).item()
        
        # Inverse transform and get the predicted visitors
        log_prediction = scaler_y.inverse_transform([[y_pred_std]])[0][0]
        prediction_original = np.expm1(log_prediction)

        return {"predicted_visitors": round(prediction_original)}

    except Exception as e:
        return {"error": str(e)}
