# Tourist Prediction App

This project provides a prediction system that estimates visitor numbers based on various inputs such as rating, revenue, and country. The system uses machine learning models (Linear Regression) to calculate expected visitors for tourist destinations.

## The project consists of:

- A Flutter mobile app for user input and predictions.

- A FastAPI backend exposing the prediction API.

- A Google Colab Notebook with model training and performance evaluation.

## Source of Data
The dataset used for training was sourced from Kaggle, containing historical visitor data, revenue figures, and customer ratings. The data was preprocessed to handle missing values, normalize numerical features, and encode categorical variables to improve model performance.

***
***

# Live Links
## API 
The public API endpoint for predictions is hosted at: [Api_link](https://linear-regression-api-o7as.onrender.com/docs)

## Video Demo
Watch the demo video showcasing how the app works and how predictions are made: [video_demo](https://www.youtube.com/watch?v=wlDl2ClFTzU&ab_channel=CceE)

## How to run Mobile App

1. Clone the repository:
   ```bash
   git clone https://github.com/Cchancee/linear_regression_model.git
   cd FlutterApp/trevo 
   ```

2. Install Flutter dependencies:
    ```
    flutter pub get
    ```

3. Connect your device or use an emulator, and run the app:
    ```
    flutter run
    ```
  
The app will now open and you can enter values for the rating, revenue, and country to receive predictions based on the model.