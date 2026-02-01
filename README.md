# Photothèque Intelligente

Système de gestion et recherche d'images basé sur l'apprentissage automatique.

Fonctionnalités:
- Ingestion d'images avec détection de doublons et optimisation
- Extraction des données EXIF et métadonnées
- OCR pour le texte présent dans les images
- Tagging automatique des images
- Recherche par similarité sémantique
- Interface web pour explorer et rechercher

Structure du projet:
- main.py: Point d'entrée principal
- config/settings.py: Configuration
- scripts/: Modules métier (ingestion, OCR, tagging, embeddings, recherche)
- ui/interface.py: Interface web
- data/: Images et résultats

Installation rapide:
1. Créez un environnement virtuel Python 3.10+
2. Installez les dépendances: `pip install -r requirements.txt`
3. Installez Tesseract OCR (Windows): https://github.com/tesseract-ocr/tesseract
4. Placez vos images dans `data/images/raw`
5. Lancez le pipeline: `python main.py --mode pipeline`
6. Lancez l'interface: `python main.py --mode ui` ou `streamlit run ui/interface.py`

Notes:
- Les modèles pré-entraînés sont téléchargés au premier lancement
- Mis en cache dans `models/cache` pour accès rapide
- Configurer Tesseract path dans `.env` si besoin de l'OCR
