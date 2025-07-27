from fastapi import APIRouter, Query
import pandas as pd
from ..models.schemas import AdFrequencyInput
from ..services.mlflow_service import predict

router = APIRouter(prefix="/predict", tags=["Ad Frequency"])

@router.post("/ad-frequency")
def predict_ad_frequency(run_id: str = Query(...), data: AdFrequencyInput = None):
    df = pd.DataFrame([data.dict()])
    result = predict(run_id, "ad_frequency", df)
    return {"user_key_id": data.user_key_id, "prediction": float(result[0])}
