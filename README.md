# 🖼️ VisualIndexer

**AI-Powered Image Management & Semantic Search with PyTorch, CLIP, Transformers & Streamlit**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.1-red)
![CLIP](https://img.shields.io/badge/CLIP-Vision--Language-orange)
![Transformers](https://img.shields.io/badge/Transformers-4.35.2-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-green)
![TensorFlow](https://img.shields.io/badge/OCR-Tesseract-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Project Description

**VisualIndexer** is a complete and intelligent system for image management, automatic indexing, and semantic search. Powered by **Artificial Intelligence** and state-of-the-art **Deep Learning** models (PyTorch, CLIP, Transformers).

This project enables:
- 📥 Batch ingest and optimize images
- 🔍 Automatically extract EXIF metadata
- 📄 Recognize text in images (OCR)
- 🏷️ Automatically generate intelligent visual tags
- 🧠 Create semantic vector representations
- ⚡ Search images by similarity
- 🎨 Explore results via an interactive web interface

---

## 🚀 Key Features

### 1️⃣ **Image Ingestion**
- Batch upload and ingest image files
- Automatic duplicate detection (MD5 hash)
- Intelligent optimization and resizing (max 1920x1080)
- Adaptive JPEG compression (quality 85%)

### 2️⃣ **Metadata Extraction**
- Complete EXIF extraction (capture date, camera, GPS, etc.)
- Image dimensions and format
- Automatic CSV generation for analysis

### 3️⃣ **Text Recognition (OCR)**
- Multi-language Tesseract OCR (English + French)
- Extract text present in images
- JSON caching for optimization

### 4️⃣ **Automatic Tagging**
- Vision Transformer CLIP (OpenAI)
- Intelligent visual tag generation
- 50+ predefined categories (city, portrait, food, document, etc.)

### 5️⃣ **Semantic Embeddings**
- 384D vector generation with Sentence-Transformers
- Semantic content representation
- Advanced similarity search

### 6️⃣ **Advanced Search Engine**
- Text search with embeddings
- Metadata filtering (date, size, format)
- Combined tag search
- Intelligent result fusion

### 7️⃣ **Interactive Web Interface**
- Modern Streamlit dashboard
- Image visualization
- Multi-criteria search
- Result export

---

## 🛠️ Technologies Used

**VisualIndexer** uses a modern and performant technology stack:
- **Python** 3.10+ - Primary language
- **Pip** - Package manager

### **Deep Learning & Vision**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **PyTorch** | 2.1.1 | Framework deep learning |
| **TorchVision** | 0.16.1 | Vision utilities |
| **Transformers** | 4.35.2 | HuggingFace models |
| **Sentence-Transformers** | 2.2.2 | Embeddings sémantiques |
| **CLIP** | 0.1.0.post1 | Vision-Language model |

### **Image Processing**
| Technology | Version | Usage |
|-------------|---------|-------|
| **Pillow** | 10.1.0 | Image manipulation |
| **OpenCV** | 4.8.1 | Vision algorithms |
| **Pytesseract** | 0.3.10 | OCR wrapper |

### **Data Science & Analytics**
| Technology | Version | Usage |
|-------------|---------|-------|
| **NumPy** | 1.26.2 | Numerical computing |
| **Pandas** | 2.1.3 | Dataframes & data processing |
| **Scikit-learn** | 1.3.2 | ML utilities |

### **Web & UI**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **Streamlit** | 1.29.0 | Interface web interactive |

### **Database & Utils**
| Technology | Version | Usage |
|-------------|---------|-------|
| **PostgreSQL** | - | (Optional) Database |
| **Python-dotenv** | 1.0.0 | Environment variables |
| **TQDM** | 4.66.1 | Progress bars |
| **Requests** | 2.31.0 | HTTP client |

### **External Infrastructure**
- **Tesseract OCR** - Optical character recognition (Windows/Linux/Mac)

---

## 📁 Project Structure

```
VisualIndexer/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── .env                    # Configuration (Tesseract path)
├── .gitignore              # Git exclusions
│
├── config/
│   └── settings.py         # Centralized configuration
│
├── scripts/                # Business logic modules
│   ├── ingest.py           # Ingestion & duplicates
│   ├── extract_metadata.py # EXIF extraction
│   ├── ocr.py              # Tesseract OCR
│   ├── tag_clip.py         # CLIP tagging
│   ├── embeddings.py       # Semantic vectors
│   └── search.py           # Search engine
│
├── ui/
│   └── interface.py        # Streamlit interface
│
├── data/
│   ├── images/
│   │   ├── raw/            # Input images
│   │   └── processed/      # Optimized images
│   ├── metadata.csv        # Metadata
│   ├── embeddings.json     # Embeddings cache
│   └── ocr_results.json    # OCR cache
│
├── models/
│   └── cache/              # ML models cache
│
├── README.md               # Documentation
├── GUIDE_UTILISATION.md    # Usage guide
└── COMMITS_GUIDE.md        # Commits guide
```

---

## ⚙️ Installation & Configuration

### Prérequis
- Python 3.10 ou supérieur
- Git
- 2GB d'espace disque (pour les modèles)

### Installation Rapide

```bash
# 1. Cloner le repo
git clone https://github.com/IlyasFardaouix/VisualIndexer.git
cd VisualIndexer

# 2. Créer environnement virtuel
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Installer Tesseract (Windows)
# Télécharger: https://github.com/tesseract-ocr/tesseract
# Installer et configurer path dans .env

# 5. Placer images
# Mettre images dans: data/images/raw/

# 6. Lancer le pipeline
python main.py --mode pipeline

# 7. Lancer l'interface web
python main.py --mode ui
# Accès: http://localhost:8501
```

---

##  Pipeline 5 Étapes

```
Images Brutes
    ↓
[1] INGESTION → Détection doublons, optimisation
    ↓
[2] MÉTADONNÉES → Extraction EXIF, CSV
    ↓
[3] OCR → Reconnaissance texte
    ↓
[4] TAGGING → CLIP vision, tags
    ↓
[5] EMBEDDINGS → Vecteurs sémantiques, recherche
    ↓
Résultats Indexés & Recherchables
```

---

## 🎯 Cas d'Usage

✅ **Archivage Intelligent** - Gestion massive d'images professionnelles  
✅ **Recherche Sémantique** - Trouver images par similarité visuelle  
✅ **Indexation Automatique** - Tags et métadonnées sans intervention  
✅ **Dédoublonnage** - Eliminer doublons détectés  
✅ **Documentation** - Extraire texte depuis documents scannés  
✅ **E-Commerce** - Cataloguer produits en images  

---

## 📝 Usage

### Full Pipeline Mode
```bash
python main.py --mode pipeline
```
Processes all images in the `data/images/raw/` folder

### Web Interface Mode
```bash
python main.py --mode ui
```
Launches the Streamlit dashboard on http://localhost:8501

### Ingestion Only Mode
```bash
python main.py --mode ingest
```
Ingests images only without AI modules

---

## 📚 Additional Documentation

- [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md) - Complete usage guide
- [COMMITS_GUIDE.md](COMMITS_GUIDE.md) - GitHub commits documentation
- [requirements.txt](requirements.txt) - Complete dependencies list

---

## 💡 Optimizations & Performance

- ✅ Intelligent ML model caching
- ✅ Reused embedding vectors
- ✅ Optimized JPEG compression
- ✅ Batch processing
- ✅ Progress tracking with TQDM

---

## 🔒 Security Configuration

Sensitive variables are stored in `.env`:
```bash
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
OCR_LANGUAGE=eng+fra
DB_HOST=localhost
DB_PORT=5432
```

---

## 📄 License

MIT License - Free to use

---

## 👤 Author

**Ilyas Fardaouix**  
GitHub: [@IlyasFardaouix](https://github.com/IlyasFardaouix)

---

## 🤝 Support & Contributions

Have questions or improvements? Open an [Issue](https://github.com/IlyasFardaouix/VisualIndexer/issues) or submit a [Pull Request](https://github.com/IlyasFardaouix/VisualIndexer/pulls)

---

**⭐ If you like this project, don't forget to star it!**
