```python
import os
import json
from PIL import Image
import pytesseract
from config.settings import TESSERACT_PATH, OCR_LANGUAGE, OCR_PATH

# Set Tesseract path for pytesseract
pytesseract.pytesseract.pytesseract_cmd = TESSERACT_PATH

class OCRProcessor:
    """
    Classe pour gérer les tâches d'OCR (Reconnaissance Optique de Caractères).
    
    Cela inclut la lecture d'images, la reconnaissance de texte et la sauvegarde des résultats.
    """
    
    def __init__(self):
        """
        Initialisation de l'instance OCRProcessor.
        
        Charge le cache OCR si disponible.
        """
        self.ocr_cache = {}  # Dictionnaire pour stocker les résultats OCR
        self._load_cached_ocr()  # Charge le cache OCR
        
    def _load_cached_ocr(self):
        """
        Charge le cache OCR si disponible.
        
        :return: None
        """
        if os.path.exists(OCR_PATH):
            try:
                with open(OCR_PATH, 'r', encoding='utf-8') as f:
                    self.ocr_cache = json.load(f)
            except Exception as e:
                print(f"Impossible de charger le cache OCR: {e}")
    
    def run_ocr(self, image_path):
        """
        Effectue l'OCR sur une image.
        
        :param image_path: Chemin d'accès à l'image
        :return: Le texte reconnu dans l'image
        """
        filename = os.path.basename(image_path)
        
        # Vérifie si le résultat est déjà dans le cache
        if filename in self.ocr_cache:
            return self.ocr_cache[filename]
        
        try:
            # Ouvre l'image
            image = Image.open(image_path)
            
            # Effectue l'OCR
            text = pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
            
            # Nettoie le texte
            text = text.strip()
            if not text:
                text = "Aucun texte détecté"
            
            # Stocke le résultat dans le cache
            self.ocr_cache[filename] = text
            
            print(f"OCR effectué: {filename}")
            return text
        
        except pytesseract.TesseractNotFoundError:
            print("Tesseract n'est pas installé. Installez-le et configurez TESSERACT_PATH")
            return "Erreur: Tesseract non disponible"
        
        except Exception as e:
            print(f"Erreur OCR sur {filename}: {e}")
            return f"Erreur OCR: {str(e)}"
    
    def save_ocr_results(self):
        """
        Sauvegarde les résultats OCR dans un fichier JSON.
        
        :return: None
        """
        try:
            with open(OCR_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.ocr_cache, f, indent=2, ensure_ascii=False)
            print(f"Résultats OCR sauvegardés: {OCR_PATH}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde OCR: {e}")


# Instance globale
ocr_processor = OCRProcessor()

def run_ocr(image_path):
    """
    Fonction de compatibilité pour effectuer l'OCR sur une image.
    
    :param image_path: Chemin d'accès à l'image
    :return: Le texte reconnu dans l'image
    """
    return ocr_processor.run_ocr(image_path)

def save_ocr_results():
    """
    Sauvegarde tous les résultats OCR.
    
    :return: None
    """
    ocr_processor.save_ocr_results()
```