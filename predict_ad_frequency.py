import mlflow
import pandas as pd
import numpy as np
import json
import os
import argparse

def download_mlflow_artifact(run_id, artifact_path, local_dir="."):
    local_path = mlflow.artifacts.download_artifacts(
        run_id=run_id,
        artifact_path=artifact_path,
        dst_path=local_dir
    )
    return local_path

def predict_with_model(run_id, raw_data_df):
    print(f"🔄 Model ve gerekli objeler yükleniyor... (Run ID: {run_id})")
    
    label_encoders_path = download_mlflow_artifact(run_id, "ad_frequency_label_encoders.json")
    run_info_path = download_mlflow_artifact(run_id, "ad_frequency_run_info.json")

    with open(label_encoders_path) as f:
        label_encoders_classes = json.load(f)
    
    with open(run_info_path) as f:
        run_info = json.load(f)

    training_columns = run_info['training_columns']
    
    print("✅ Objeler başarıyla yüklendi.")
    print("🛠️  Tahmin verisi işleniyor...")
    
    processed_df = raw_data_df.copy()
    
    for col, classes in label_encoders_classes.items():
        class_map = {label: i for i, label in enumerate(classes)}
        processed_df[col] = processed_df[col].map(class_map)

    processed_df = processed_df.reindex(columns=training_columns, fill_value=0)
    
    print("✅ Veri başarıyla işlendi.")

    model_uri = f"runs:/{run_id}/model"
    loaded_model = mlflow.sklearn.load_model(model_uri)
    
    predictions = loaded_model.predict(processed_df.values)
    return predictions

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Personalized Ad Frequency Model Predictor")
    parser.add_argument("--run_id", type=str, required=True, help="MLflow Run ID")
    args = parser.parse_args()

    # Örnek kullanıcı verisi
    sample_raw_data = pd.DataFrame({
        'user_key_id': ['bVas4SMsXQ'],
        'country': ['GB'],
        'age': [30],
        'sex': ['Men'],
        'easy_completion_rate': [100],
        'medium_completion_rate': [100],
        'hard_completion_rate': [25],
        'session_count': [86],
        'total_session_time': [52464],
        'total_ad_viewed': [15],
        'total_earned_reward_amount_in_usd': [18.68]
    })

    print("\n--- Tahmin Sonuçları ---")
    try:
        predictions = predict_with_model(args.run_id, sample_raw_data)
        print(f"Kullanıcı {sample_raw_data['user_key_id'].iloc[0]} için tahmin edilen değer: {predictions[0]}")
    except Exception as e:
        print("\n❌ HATA: Tahmin yapılırken bir sorun oluştu.")
        print(f"Detay: {e}")
