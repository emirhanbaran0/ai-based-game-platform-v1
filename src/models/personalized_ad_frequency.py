from .base_model import BaseModel
from sklearn.cluster import DBSCAN

class DBSCANClusterer(BaseModel):
    def _create_model(self):
        return DBSCAN(**self.params)

MODEL_REGISTRY = {
    "DBSCANClusterer": DBSCANClusterer,
}