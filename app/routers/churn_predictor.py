from fastapi import APIRouter, Query
import pandas as pd
from ..models.schemas import ChurnInput
from ..services.mlflow_service import predict

router = APIRouter(prefix="/predict", tags=["Churn Predictor"])

@router.post("/churn-predictor")
def predict_churn(run_id: str = Query(...), data: ChurnInput = None):
    df = pd.DataFrame([data.dict()])
    result = predict(run_id, "churn_predictor", df)
    return {"user_key_id": data.user_key_id, "prediction": float(result[0])}
