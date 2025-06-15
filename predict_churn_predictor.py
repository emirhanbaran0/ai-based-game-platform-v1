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

    training_columns = run_info['training_columns']
    
    print("✅ Objeler başarıyla yüklendi.")
    
    print("🛠️  Tahmin verisi işleniyor...")
    processed_df = raw_data_df.copy()
    processed_df['first_time_login'] = pd.to_datetime(processed_df['first_time_login'])
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


    sample_raw_data = pd.DataFrame({
    'user_key_id': ['CDMl6fGsuz'],
    'country': ['DE'],
    'age': [36],
    'sex': ['Men'],
    'first_time_login': ['2025-03-22 08:06:23'],
    'session_count': [81],
    'total_session_time_x': [100811],
    'total_ad_viewed': [536],
    'total_spent_in_usd': [0],
    'total_spent_time': [0],
    'total_session_time_y': [100811],
    'level_completion_count': [9],
    'avg_level_completion_time': [11201.22222],
    'easy_completion_rate': [100],
    'medium_completion_rate': [50],
    'hard_completion_rate': [0],
})

    sample_raw_data1 = pd.DataFrame({
    'user_key_id': ['wFfzWC1Ydt'],
    'country': ['US'],
    'age': [18],
    'sex': ['Men'],
    'first_time_login': ['2025-04-10 02:16:18'],
    'session_count': [65],
    'total_session_time_x': [15986],
    'total_ad_viewed': [30],
    'total_spent_in_usd': [0],
    'total_spent_time': [0],
    'total_session_time_y': [75586],
    'level_completion_count': [8],
    'avg_level_completion_time': [12597.66667],
    'easy_completion_rate': [25],
    'medium_completion_rate': [0],
    'hard_completion_rate': [0],
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