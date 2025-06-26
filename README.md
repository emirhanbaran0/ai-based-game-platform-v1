# 🎮 AI-Based Game Platform

Bu proje, oyuncu davranışlarını analiz ederek kişiselleştirilmiş oyun deneyimi sunmayı amaçlayan bir yapay zeka tabanlı oyun platformudur. Kullanıcıların **oyunu bırakma (churn)** ihtimalleri tahmin edilir ve **reklam sıklığı**, **uygulama içi satın alım paketleri (IAP)** ve **seviye zorlukları** gibi unsurlar kişiselleştirilir.

---

## 🔍 Özellikler

- 🎯 Oyuncu churn (terk etme) tahmini
- 🧠 Kişiselleştirilmiş reklam gösterimi frekansı önerileri
- 💸 Kullanıcıya özel IAP (In-App Purchase) paket önerileri
- 🎮 Oyuncuya özel zorluk seviyesi ayarlamaları
- 🗃️ MLflow ile deneyim yönetimi ve kayıt
- 📁 SQL tabanlı veri yapısı desteği
- 📊 JSON tabanlı etiketleyici (label encoder) ve model kayıt sistemi

---

## 📁 Proje Yapısı

ai-based-game-platform/
│
├── src/
│ ├── data_preprocess/ # Veri ön işleme scriptleri
│ ├── models/ # Model tanımlamaları
│ └── utils.py # Yardımcı fonksiyonlar
│
├── prediction/
│ ├── predict_churn_predictor.py
│ ├── predict_iap_packs.py
│ ├── predict_ad_frequency.py
│ └── predict_level_difficulty.py
│
├── configs/ # Model konfigürasyon dosyaları (YAML)
│
├── mlruns/ # MLflow deneyim klasörü
├── saved_models/ # Eğitilmiş modeller
├── data/ # Veri setleri
│
├── personalized_ad_frequency.ipynb
├── personalized_iap_packs.ipynb
├── personalized_level_difficulty.ipynb
│
├── ai_based_game_platform_data_sql.sql
├── train_churn_predictor.py
├── requirements.txt
├── *.json # Etiketleyici ve deneyim bilgileri



---

## 🚀 Kurulum

### 1. Gereksinimler

Python 3.8+ gereklidir. Gerekli bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt


⚙️ Kullanım
Churn Modeli Eğitimi
bash
Kopyala
Düzenle
python train_churn_predictor.py
Tahmin Scriptleri
bash
Kopyala
Düzenle
python prediction/predict_churn_predictor.py
python prediction/predict_ad_frequency.py
python prediction/predict_iap_packs.py
python prediction/predict_level_difficulty.py
Jupyter Notebooklar
Modellerin çalışma şeklini incelemek ve kişiselleştirme adımlarını görmek için aşağıdaki dosyaları kullanabilirsiniz:

personalized_ad_frequency.ipynb

personalized_iap_packs.ipynb

personalized_level_difficulty.ipynb

🧪 MLflow Kullanımı
MLflow ile model eğitimi ve deneyimleri takip edilebilir. UI arayüzünü çalıştırmak için:

bash
Kopyala
Düzenle
mlflow ui
Sonrasında http://localhost:5000 adresinden arayüze erişebilirsiniz.

📌 Notlar
Etiketleyiciler (LabelEncoders) .json formatında saklanmaktadır.

Konfigürasyonlar configs/ klasöründe YAML formatında yer almaktadır.

Kodlar modüler yapıdadır ve yeni modellerin kolayca entegre edilebilmesi için ölçeklenebilir tasarlanmıştır.

Model dosyaları ve deneyim kayıtları saved_models/ ve mlruns/ klasörlerinde tutulmaktadır.

👤 Geliştirici
Emirhan Baran
GitHub: @emirhanbaran0