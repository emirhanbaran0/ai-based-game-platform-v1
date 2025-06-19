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

    config = load_config("configs/churn_experiments.yaml")
    
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
        label_encoders[col] = list(le.classes_)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.set_experiment(config['experiment_name'])
    
    for model_config in config['models']:
        model_name = model_config['model_name']
        ModelClass = MODEL_REGISTRY[model_name]
        
        for params in model_config['param_grid']:
            with mlflow.start_run():
                print(f"\nÇalıştırılan Deney: Model={model_name}, Parametreler={params}")
                
                mlflow.log_params(params)
                mlflow.set_tag("model_name", model_name)
                
                model = ModelClass(params)
                model.train(X_train, y_train)
                
                predictions = model.predict(X_test)
                metrics = evaluate_model(y_test, predictions)
                
                mlflow.log_metrics(metrics)
                print(f"Sonuçlar: {metrics}")
                
                mlflow.sklearn.log_model(model.model, "model")

                mlflow.log_dict(label_encoders, "churn_predictor_label_encoders.json")

                run_info = {
                    "training_columns": list(X.columns)
                }
                mlflow.log_dict(run_info, "churn_predictor_run_info.json")

    print("\nTüm deneyler tamamlandı. Sonuçları görmek için terminale 'mlflow ui' yazın.")

if __name__ == "__main__":
    main()