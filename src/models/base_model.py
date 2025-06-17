from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Tüm makine öğrenmesi modelleri için temel arayüz (template)."""
    
    def __init__(self, params):
        self.params = params
        self.model = self._create_model()

    @abstractmethod
    def _create_model(self):
        """Model nesnesini parametrelerle başlatır."""
        pass

    def train(self, X_train, y_train):
        """Modeli eğitir."""
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """Tahmin yapar."""
        return self.model.predict(X)

    def predict_proba(self, X):
        """Olasılık tahmini yapar."""
        return self.model.predict_proba(X)
    
    def fit_predict(self, X):
        """Clustering yapar"""
        return self.model.fit_predict(X)