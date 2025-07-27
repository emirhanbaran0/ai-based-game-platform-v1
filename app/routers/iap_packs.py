from fastapi import APIRouter, Query
import pandas as pd
from ..models.schemas import IAPPackInput
from ..services.mlflow_service import predict

router = APIRouter(prefix="/predict", tags=["IAP Packs"])

@router.post("/iap-packs")
def predict_iap_packs(run_id: str = Query(...), data: IAPPackInput = None):
    df = pd.DataFrame([data.dict()])
    result = predict(run_id, "iap_packs", df)
    return {"user_key_id": data.user_key_id, "prediction": float(result[0])}
