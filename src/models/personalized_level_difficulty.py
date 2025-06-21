from sklearn.cluster import KMeans, SpectralClustering
from .base_model import BaseModel

class KMeansClusterer(BaseModel):
    def _create_model(self):
        return KMeans(**self.params)

class SpectralClusterer(BaseModel):
    def _create_model(self):
        return SpectralClustering(**self.params) 

MODEL_REGISTRY = {
    "KMeansClusterer": KMeansClusterer,
    "SpectralClusterer" : SpectralClusterer
}
    