# Project Name

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/yourusername/your-repo-name)  
A machine learning project with an API endpoint for predictions and a Flutter mobile app.

---

## Project Overview
This repository contains:
- **Jupyter Notebook**: Model training and evaluation.
- **API Code**: FastAPI/Flask code for serving predictions.
- **Flutter App**: Mobile app to interact with the API.

---

## API Endpoint
A publicly available API endpoint is deployed for live predictions. Use the link below to test it via **Swagger UI**:  

🔗 **Endpoint URL**: `https://your-api-name.herokuapp.com/docs`  

**Example Request**:
```bash
POST /predict
Content-Type: application/json

{
  "feature_1": 5.1,
  "feature_2": 3.5,
  "feature_3": 1.4,
  "feature_4": 0.2
}
