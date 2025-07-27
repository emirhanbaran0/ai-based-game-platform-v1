import mlflow
import pandas as pd
import json
import os

# Cache for loaded models and metadata
_model_cache = {}

# Map prefixes to artifact file names
ARTIFACT_MAP = {
    "ad_frequency": {
        "label": "ad_frequency_label_encoders.json",
        "info": "ad_frequency_run_info.json"
    },
    "churn_predictor": {
        "label": "churn_predictor_label_encoders.json",
        "info": "churn_predictor_run_info.json"
    },
    "iap_packs": {
        "label": "iap_packs_label_encoders.json",
        "info": "iap_packs_run_info.json"
    },
    "level_difficulty": {
        "label": "level_difficulty_label_encoders.json",
        "info": "level_difficulty_run_info.json"
    }
}


def download_mlflow_artifact(run_id, artifact_path, local_dir="."):
    """Download artifact from MLflow and return its local path."""
    return mlflow.artifacts.download_artifacts(
        run_id=run_id,
        artifact_path=artifact_path,
        dst_path=local_dir
    )


def load_model(run_id: str, prefix: str):
    """Load model and its metadata, with caching for speed."""
    cache_key = f"{run_id}_{prefix}"
    if cache_key in _model_cache:
        return _model_cache[cache_key]

    if prefix not in ARTIFACT_MAP:
        raise ValueError(f"Invalid model prefix: {prefix}")

    # Download artifacts
    label_file = ARTIFACT_MAP[prefix]["label"]
    info_file = ARTIFACT_MAP[prefix]["info"]

    label_encoders_path = download_mlflow_artifact(run_id, label_file)
    run_info_path = download_mlflow_artifact(run_id, info_file)

    if not label_encoders_path or not run_info_path:
        raise FileNotFoundError(f"Required artifacts missing for prefix: {prefix}")

    # Load artifacts
    with open(label_encoders_path) as f:
        label_encoders_classes = json.load(f)
    with open(run_info_path) as f:
        run_info = json.load(f)

    # Load model
    model_uri = f"runs:/{run_id}/model"
    model = mlflow.sklearn.load_model(model_uri)

    _model_cache[cache_key] = (model, label_encoders_classes, run_info)
    return _model_cache[cache_key]


def preprocess(df: pd.DataFrame, label_encoders_classes: dict, training_columns: list, drop_cols: list = []):
    """Preprocess input data for prediction."""
    processed_df = df.copy()

    # Drop unnecessary columns if any
    if drop_cols:
        processed_df = processed_df.drop(columns=drop_cols, errors='ignore')

    # Encode categorical columns
    for col, classes in label_encoders_classes.items():
        class_map = {label: i for i, label in enumerate(classes)}
        processed_df[col] = processed_df[col].map(class_map).fillna(-1)  # unknown -> -1

    # Align with training columns
    processed_df = processed_df.reindex(columns=training_columns, fill_value=0)

    # Fill any remaining NaN
    processed_df = processed_df.fillna(0)

    return processed_df


def predict(run_id: str, prefix: str, df: pd.DataFrame, drop_cols: list = []):
    """Make predictions using MLflow model."""
    model, label_encoders_classes, run_info = load_model(run_id, prefix)
    processed_df = preprocess(df, label_encoders_classes, run_info['training_columns'], drop_cols)
    return model.predict(processed_df)
