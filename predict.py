import mlflow
import pandas as pd
import numpy as np
import json
import os
import argparse # <-- GEREKLİ KÜTÜPHANEYİ İÇERİ AKTAR

def download_mlflow_artifact(run_id, artifact_path, local_dir="."):
    """MLflow'dan bir artifact'i indirir ve yerel yolunu döndürür."""
    local_path = mlflow.artifacts.download_artifacts(
        run_id=run_id,
        artifact_path=artifact_path,
        dst_path=local_dir
    )
    return local_path

def predict_with_model(run_id, raw_data_df):
    """
    Modeli ve gerekli objeleri MLflow'dan yükler, veriyi işler ve tahmin yapar.
    """
    print(f"🔄 Model ve gerekli objeler yükleniyor... (Run ID: {run_id})")

    # Gerekli objeleri yükle... (Bu kısım öncekiyle aynı)
    label_encoders_path = download_mlflow_artifact(run_id, "label_encoders.json")
    run_info_path = download_mlflow_artifact(run_id, "run_info.json")

    with open(label_encoders_path) as f:
        label_encoders_classes = json.load(f)
    
    with open(run_info_path) as f:
        run_info = json.load(f)

    min_login_date = pd.to_datetime(run_info['min_login_date'])
    training_columns = run_info['training_columns']
    
    print("✅ Objeler başarıyla yüklendi.")
    
    print("🛠️  Tahmin verisi işleniyor...")
    processed_df = raw_data_df.copy()
    processed_df['first_time_login'] = pd.to_datetime(processed_df['first_time_login'])
    processed_df['days_since_first_login'] = (processed_df['first_time_login'] - min_login_date).dt.days
    processed_df = processed_df.drop(columns=['first_time_login'])

    for col, classes in label_encoders_classes.items():
        class_map = {label: i for i, label in enumerate(classes)}
        processed_df[col] = processed_df[col].map(class_map)

    processed_df = processed_df.reindex(columns=training_columns, fill_value=0)
    print("✅ Veri başarıyla işlendi.")

    model_uri = f"runs:/{run_id}/model"
    loaded_model = mlflow.sklearn.load_model(model_uri)
    
    predictions = loaded_model.predict(processed_df)
    return predictions

if __name__ == '__main__':
    # --- YENİ: KOMUT SATIRI ARGÜMANLARINI TANIMLAMA ---
    parser = argparse.ArgumentParser(description="MLflow'daki bir modelle tahmin yap.")
    parser.add_argument(
        "--run_id", 
        type=str, 
        required=True, 
        help="MLflow'dan alınacak modelin Run ID'si."
    )
    args = parser.parse_args()
    # ----------------------------------------------------

    # Tahmin yapılacak yeni HAM kullanıcı verisi
    sample_raw_data = pd.DataFrame({
        'user_key_id': [98765],
        'country': ['Germany'],
        'sex': ['Male'],
        'age': [34],
        'first_time_login': ['2025-05-10'],
        'total_session_time_x': [5500.0]
        # ... modelin beklediği diğer ham sütunlar ...
    })

    print("\n--- Tahmin Sonuçları ---")
    try:
        # Değişkeni hard-code yerine argümandan alıyoruz
        predictions = predict_with_model(args.run_id, sample_raw_data)
        
        for i, pred in enumerate(predictions):
            churn_status = "Oyunu Bırakacak" if pred == 1 else "Oyuna Devam Edecek"
            print(f"Kullanıcı {sample_raw_data['user_key_id'].iloc[i]} Tahmini: {churn_status}")

    except Exception as e:
        print(f"\n❌ HATA: Tahmin yapılırken bir sorun oluştu.")
        print(f"Detay: {e}")