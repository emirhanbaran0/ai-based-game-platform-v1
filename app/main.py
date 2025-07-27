from fastapi import FastAPI
from .routers import ad_frequency, churn_predictor, iap_packs, level_difficulty

app = FastAPI(title="ML Prediction API")

# Register routers
app.include_router(ad_frequency.router)
app.include_router(churn_predictor.router)
app.include_router(iap_packs.router)
app.include_router(level_difficulty.router)
