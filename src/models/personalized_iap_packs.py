from sklearn.cluster import KMeans
from .base_model import BaseModel

class KMeansClusterer(BaseModel):
    def _create_model(self):
        return KMeans(**self.params)
    

MODEL_REGISTRY = {
    "KMeansClusterer": KMeansClusterer,
}
    