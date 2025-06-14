from .base_model import BaseModel
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression

class RandomForestPredictor(BaseModel):
    def _create_model(self):
        return RandomForestClassifier(**self.params)

class XGBoostPredictor(BaseModel):
    def _create_model(self):
        return XGBClassifier(use_label_encoder=False, eval_metric='logloss', **self.params)


class LogisticRegressionPredictor(BaseModel):
    def _create_model(self):
        return LogisticRegression(**self.params)


MODEL_REGISTRY = {
    "RandomForestClassifier": RandomForestPredictor,
    "XGBClassifier": XGBoostPredictor,
    "LogisticRegression": LogisticRegressionPredictor, 
}