# 🖼️ VisualIndexer

**AI-Powered Image Management & Semantic Search with PyTorch, CLIP, Transformers & Streamlit**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.1-red)
![CLIP](https://img.shields.io/badge/CLIP-Vision--Language-orange)
![Transformers](https://img.shields.io/badge/Transformers-4.35.2-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-green)
![TensorFlow](https://img.shields.io/badge/OCR-Tesseract-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Description du Projet

**VisualIndexer** est un système complet et intelligent de gestion, indexation automatique et recherche sémantique d'images. Propulsé par l'**Intelligence Artificielle** et les modèles **Deep Learning** dernière génération (PyTorch, CLIP, Transformers). 

Ce projet permet de:
- 📥 Ingérer et optimiser des images en masse
- 🔍 Extraire automatiquement des métadonnées EXIF
- 📄 Reconnaître du texte dans les images (OCR)
- 🏷️ Générer automatiquement des tags visuels intelligents
- 🧠 Créer des représentations vectorielles sémantiques
- ⚡ Rechercher des images par similarité
- 🎨 Explorer les résultats via une interface web interactive

---

## 🚀 Fonctionnalités Principales

### 1️⃣ **Ingestion d'Images**
- Upload/ingestion en masse de fichiers images
- Détection automatique des doublons (hash MD5)
- Optimisation et redimensionnement intelligent (max 1920x1080)
- Compression JPEG adaptée (qualité 85%)

### 2️⃣ **Extraction de Métadonnées**
- Extraction EXIF complète (date prise, appareil photo, GPS, etc.)
- Dimensions et format d'image
- Génération automatique de CSV pour analyse

### 3️⃣ **Reconnaissance de Texte (OCR)**
- OCR Tesseract multi-langue (Français + Anglais)
- Extraction du texte présent dans les images
- Cache JSON pour optimisation

### 4️⃣ **Tagging Automatique**
- Vision Transformer CLIP (OpenAI)
- Génération de tags visuels intelligents
- 50+ catégories prédéfinies (ville, portrait, nourriture, document, etc.)

### 5️⃣ **Embeddings Sémantiques**
- Génération de vecteurs 384D avec Sentence-Transformers
- Représentation sémantique du contenu
- Recherche par similarité avancée

### 6️⃣ **Moteur de Recherche Avancée**
- Recherche par texte avec embeddings
- Filtrage par métadonnées (date, taille, format)
- Recherche par tags combinée
- Fusion intelligente des résultats

### 7️⃣ **Interface Web Interactive**
- Dashboard Streamlit moderne
- Visualisation des images
- Recherche multi-critères
- Export des résultats

---

## 🛠️ Technologies Utilisées

**VisualIndexer** utilise un stack technologique moderne et performant:
- **Python** 3.10+ - Langage principal
- **Pip** - Gestionnaire de dépendances

### **Deep Learning & Vision**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **PyTorch** | 2.1.1 | Framework deep learning |
| **TorchVision** | 0.16.1 | Vision utilities |
| **Transformers** | 4.35.2 | HuggingFace models |
| **Sentence-Transformers** | 2.2.2 | Embeddings sémantiques |
| **CLIP** | 0.1.0.post1 | Vision-Language model |

### **Traitement d'Images**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **Pillow** | 10.1.0 | Manipulation d'images |
| **OpenCV** | 4.8.1 | Algorithmique vision |
| **Pytesseract** | 0.3.10 | OCR wrapper |

### **Data Science & Analytics**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **NumPy** | 1.26.2 | Calcul numérique |
| **Pandas** | 2.1.3 | Frames & données |
| **Scikit-learn** | 1.3.2 | ML utilities |

### **Web & UI**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **Streamlit** | 1.29.0 | Interface web interactive |

### **Database & Utils**
| Technologie | Version | Usage |
|-------------|---------|-------|
| **PostgreSQL** | - | (Optionnel) Base de données |
| **Python-dotenv** | 1.0.0 | Variables d'environnement |
| **TQDM** | 4.66.1 | Progress bars |
| **Requests** | 2.31.0 | HTTP client |

### **Infrastructure Externe**
- **Tesseract OCR** - Reconnaissance optique de caractères (Windows/Linux/Mac)

---

##  Structure du Projet

```
phototheque_intelligente/
├── main.py                 # Point d'entrée principal
├── requirements.txt        # Dépendances Python
├── .env                    # Configuration (Tesseract path)
├── .gitignore             # Exclusions Git
│
├── config/
│   └── settings.py        # Configuration centralisée
│
├── scripts/               # Modules métier
│   ├── ingest.py         # Ingestion & doublons
│   ├── extract_metadata.py # Extraction EXIF
│   ├── ocr.py            # OCR Tesseract
│   ├── tag_clip.py       # Tagging CLIP
│   ├── embeddings.py     # Vecteurs sémantiques
│   └── search.py         # Moteur de recherche
│
├── ui/
│   └── interface.py      # Interface Streamlit
│
├── data/
│   ├── images/
│   │   ├── raw/          # Images d'entrée
│   │   └── processed/    # Images optimisées
│   ├── metadata.csv      # Métadonnées
│   ├── embeddings.json   # Cache embeddings
│   └── ocr_results.json  # Cache OCR
│
├── models/
│   └── cache/            # Cache modèles ML
│
├── README.md             # Documentation
├── GUIDE_UTILISATION.md  # Guide complet
└── COMMITS_GUIDE.md      # Guide des commits
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

## 📝 Utilisation

### Mode Pipeline Complet
```bash
python main.py --mode pipeline
```
Traite toutes les images du dossier `data/images/raw/`

### Mode Interface Web
```bash
python main.py --mode ui
```
Lance le dashboard Streamlit sur http://localhost:8501

### Mode Ingestion Seule
```bash
python main.py --mode ingest
```
Ingère uniquement les images sans les modules IA

---

## 📚 Documentation Additionnelle

- [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md) - Guide complet d'utilisation
- [COMMITS_GUIDE.md](COMMITS_GUIDE.md) - Documentation des commits GitHub
- [requirements.txt](requirements.txt) - Liste complète des dépendances

---

## 💡 Optimisations & Performance

- ✅ Cache intelligent des modèles ML
- ✅ Vecteurs embeddings réutilisés
- ✅ Compression JPEG optimisée
- ✅ Batch processing
- ✅ Progress tracking avec TQDM

---

## 🔒 Configuration Sécurité

Les variables sensibles sont stockées dans `.env`:
```bash
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
OCR_LANGUAGE=fra+eng
DB_HOST=localhost
DB_PORT=5432
```

---

## 📄 License

MIT License - Libre d'utilisation

---

## 👤 Auteur

**Ilyas Fardaouix**  
GitHub: [@IlyasFardaouix](https://github.com/IlyasFardaouix)

---

## 🤝 Support & Contributions

Des questions ou améliorations? Ouvrez une [Issue](https://github.com/IlyasFardaouix/Phototheque-Intelligente/issues) ou un [Pull Request](https://github.com/IlyasFardaouix/Phototheque-Intelligente/pulls)

---

**⭐ Si ce projet vous plaît, n'hésitez pas à le mettre en favori!**
