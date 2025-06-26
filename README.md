
# AI-Based Game Platform v1

Bu proje, oyunlar için oyuncu davranışını analiz edip kişiselleştirilmiş öneriler sunan makine öğrenimi modelleri geliştirmeyi ve deploy etmeyi hedefler. Özellikle:
- Oyuncu kaybını (churn) tahmin etme
- Kişiselleştirilmiş reklam sıklığı önerisi
- Kişiselleştirilmiş IAP (In-App Purchase) paket önerisi
- Kişiselleştirilmiş seviye zorluk önerisi

## Proje Yapısı

```
ai-based-game-platform-v1/
├── configs/                # Model konfigürasyon dosyaları (.yaml)
├── data/                   # Ham ve işlenmiş veri
│   ├── raw/                # Ham veri dosyaları (Excel)
│   └── processed/          # İşlenmiş veri ve ara çıktılar
├── mlruns/                 # MLflow deneme kayıtları
├── prediction/             # Eğitimli modellerle tahmin (prediction) scriptleri
├── saved_models/           # Kaydedilmiş modeller
├── src/
│   ├── data_preprocess/    # Veri hazırlama ve işleme notebookları
│   ├── models/             # Model kodları
│   └── utils.py            # Yardımcı fonksiyonlar
├── personalized_*.ipynb    # Ana model eğitim notebookları
├── train_churn_predictor.py # Churn modelini eğitim scripti
├── requirements.txt        # Gerekli Python paketleri
└── ai_based_game_platform_data_sql.sql # Örnek veri tabanı scripti
```

## Kurulum

### 1. Ortamı Hazırlama

Python 3.8+ önerilir. Aşağıdaki adımlar ile sanal ortam oluşturup bağımlılıkları kurabilirsin:

```bash
python -m venv venv
source venv/bin/activate     # (Windows için: venv\Scripts\activate)
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Gerekli Dizinler ve Dosyalar

- `data/raw/` altında .xlsx veri dosyalarının olması gerekir. Örnek veri dosyaları projede mevcuttur.
- Eğer kendi verinizi kullanacaksanız, dosya adları ve formatları notebook ve scriptlerdeki ile uyumlu olmalı.

### 3. Modelleri Eğitme

Her bir görevin eğitimini aşağıdaki Jupyter notebookları ile yapabilirsin:

- **Kişiselleştirilmiş Reklam Sıklığı:** `personalized_ad_frequency.ipynb`
- **Kişiselleştirilmiş IAP Paketleri:** `personalized_iap_packs.ipynb`
- **Kişiselleştirilmiş Seviye Zorluk:** `personalized_level_difficulty.ipynb`
- **Oyuncu Kaybı (Churn) Tahmini:** `train_churn_predictor.py` veya `src/data_preprocess/data_processing_churn_predictor.ipynb`

Model eğitimleri tamamlandığında, eğitimli modeller `saved_models/` klasörüne kaydedilir.

### 4. Modellerle Tahmin (Prediction) Yapmak

Modeller eğitildikten sonra, ilgili prediction scriptleri ile yeni oyuncular için tahminler üretebilirsin.

Örnek kullanım:

```bash
python prediction/predict_churn_predictor.py
python prediction/predict_iap_packs.py
python prediction/predict_ad_frequency.py
python prediction/predict_level_difficulty.py
```

Bu scriptler, varsayılan olarak `saved_models/` klasöründeki eğitimli modelleri ve uygun girdileri kullanır.

### 5. MLflow Kullanımı (İsteğe Bağlı)

Model denemelerini, sonuçlarını ve parametrelerini takip etmek için MLflow entegre edilmiştir. MLflow arayüzünü başlatmak için:

```bash
mlflow ui
```

ve tarayıcınızda [localhost:5000](http://localhost:5000) adresini açabilirsiniz.

### 6. Konfigürasyon Dosyaları

Her modelin yapılandırması için `configs/` klasöründeki ilgili `.yaml` dosyalarını düzenleyebilirsiniz.

### 7. Notlar

- Projede **pandas, scikit-learn, xgboost, pyyaml, mlflow, openpyxl** gibi temel veri bilimi ve ML kütüphaneleri kullanılmaktadır.
- Veriler, modeller ve çıktıların yol ve adlandırmaları üzerinde çalışırken dikkatli olun.
- Herhangi bir .ipynb dosyasını açıp çalıştırmak için Jupyter Notebook veya JupyterLab kurulu olmalı.

## Gereksinimler

`requirements.txt` dosyasındaki başlıca paketler:
- pandas
- openpyxl
- scikit-learn
- xgboost
- pyyaml
- mlflow

Yükleme için:

```bash
pip install -r requirements.txt
```

---

## İletişim

emir.baran255@gmail.com

---