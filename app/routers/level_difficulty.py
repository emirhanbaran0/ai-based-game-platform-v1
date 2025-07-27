from fastapi import APIRouter, Query
import pandas as pd
from ..models.schemas import LevelDifficultyInput
from ..services.mlflow_service import predict

router = APIRouter(prefix="/predict", tags=["Level Difficulty"])

@router.post("/level-difficulty")
def predict_level_difficulty(run_id: str = Query(...), data: LevelDifficultyInput = None):
    df = pd.DataFrame([data.dict()])
    result = predict(run_id, "level_difficulty", df)
    return {"user_key_id": data.user_key_id, "prediction": float(result[0])}
