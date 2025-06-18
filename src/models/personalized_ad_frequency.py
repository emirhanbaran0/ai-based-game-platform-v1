from .base_model import BaseModel
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans, AgglomerativeClustering, MeanShift
from sklearn.mixture import GaussianMixture

class DBSCANClusterer(BaseModel):
    def _create_model(self):
        return DBSCAN(**self.params) 
    
class KMeansClusterer(BaseModel):
    def _create_model(self):
        return KMeans(**self.params)
    
class AgglomerativeClusterer(BaseModel):
    def _create_model(self):
        return AgglomerativeClustering(**self.params)

class MeanShiftClusterer(BaseModel):
    def _create_model(self):
        return MeanShift(**self.params)

class GaussianMixtureClusterer(BaseModel):
    def _create_model(self):
        return GaussianMixture(**self.params)
    
MODEL_REGISTRY = {
    "DBSCANClusterer": DBSCANClusterer,
    "AgglomerativeClusterer": AgglomerativeClusterer,
    "KMeansClusterer": KMeansClusterer,
    "MeanShiftClusterer": MeanShiftClusterer,
    "GaussianMixtureClusterer": GaussianMixtureClusterer,
}
