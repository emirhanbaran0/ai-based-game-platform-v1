import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import os

from src.utils import load_config
from src.models.churn_predictor import MODEL_REGISTRY

def evaluate_model(y_true, y_pred):
    """Model performans metriklerini hesaplar."""
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1_score": f1}

def main():
    """Ana eğitim ve deney takip süreci."""
    # Yapılandırmayı yükle
    config = load_config("configs/churn_experiments.yaml")
    
    # Veri seti yoksa hata logu basar.
    processed_data_path = config['processed_data_path']
    if not os.path.exists(processed_data_path):
        print(f"❌ HATA: Gerekli bir dosya bulunamadı -> {processed_data_path}")
        return None
        
    # Veriyi yükle
    df = pd.read_csv(processed_data_path)
    X = df.drop(columns=[config['target_column']])
    y = df[config['target_column']]
    
    label_encoders = {}
    for col in ['country', 'sex']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        # YENİ: Encoder'ın öğrendiği sınıfları (kategorileri) sakla
        label_encoders[col] = list(le.classes_)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # MLflow deneyini başlat
    mlflow.set_experiment(config['experiment_name'])
    
    # Yapılandırma dosyasındaki her bir model ve parametre seti için döngü
    for model_config in config['models']:
        model_name = model_config['model_name']
        ModelClass = MODEL_REGISTRY[model_name]
        
        for params in model_config['param_grid']:
            with mlflow.start_run():
                print(f"\nÇalıştırılan Deney: Model={model_name}, Parametreler={params}")
                
                # MLflow'a parametreleri kaydet
                mlflow.log_params(params)
                mlflow.set_tag("model_name", model_name)
                
                # Modeli oluştur ve eğit
                model = ModelClass(params)
                model.train(X_train, y_train)
                
                # Test verisiyle tahmin yap ve metrikleri hesapla
                predictions = model.predict(X_test)
                metrics = evaluate_model(y_test, predictions)
                
                # Metrikleri MLflow'a kaydet
                mlflow.log_metrics(metrics)
                print(f"Sonuçlar: {metrics}")
                
                # Modeli MLflow'a bir 'artifact' olarak kaydet
                mlflow.sklearn.log_model(model.model, "model")

                 # LabelEncoder sınıflarını JSON olarak kaydet
                mlflow.log_dict(label_encoders, "label_encoders.json")

                # Tahmin için gerekli diğer bilgileri JSON olarak kaydet
                run_info = {
                    "training_columns": list(X.columns)
                }
                mlflow.log_dict(run_info, "run_info.json")

    print("\nTüm deneyler tamamlandı. Sonuçları görmek için terminale 'mlflow ui' yazın.")

if __name__ == "__main__":
    main()