"""
Configuration centralisée du projet Photothèque Intelligente.
Gère les chemins, les paramètres et les configurations d'environnement.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Chemins de base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Répertoires de données
IMAGE_DIR = os.path.join(BASE_DIR, 'data', 'images', 'raw')
PROCESSED_IMAGE_DIR = os.path.join(BASE_DIR, 'data', 'images', 'processed')
METADATA_PATH = os.path.join(BASE_DIR, 'data', 'metadata.csv')
EMBEDDING_PATH = os.path.join(BASE_DIR, 'data', 'embeddings.json')
OCR_PATH = os.path.join(BASE_DIR, 'data', 'ocr_results.json')

# Configuration des modèles IA
MODEL_CACHE_DIR = os.path.join(BASE_DIR, 'models', 'cache')
CLIP_MODEL = 'ViT-B/32'
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'

# Configuration OCR
TESSERACT_PATH = os.getenv('TESSERACT_PATH', r'C:\Program Files\Tesseract-OCR\tesseract.exe')
OCR_LANGUAGE = os.getenv('OCR_LANGUAGE', 'fra+eng')

# Configuration de la base de données
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('DB_NAME', 'phototheque_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

# Paramètres de traitement
BATCH_SIZE = 32
MAX_IMAGE_SIZE = (1920, 1080)
IMAGE_QUALITY = 85
SIMILARITY_THRESHOLD = 0.85

# Paramètres de sécurité
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100 MB

# Création des répertoires nécessaires
DIRS_TO_CREATE = [
    IMAGE_DIR,
    PROCESSED_IMAGE_DIR,
    os.path.dirname(METADATA_PATH),
    MODEL_CACHE_DIR,
    os.path.join(BASE_DIR, 'logs')
]

for directory in DIRS_TO_CREATE:
    os.makedirs(directory, exist_ok=True)