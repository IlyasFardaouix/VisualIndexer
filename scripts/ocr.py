import os
import json
from PIL import Image
import pytesseract
from config.settings import TESSERACT_PATH, OCR_LANGUAGE, OCR_PATH

pytesseract.pytesseract.pytesseract_cmd = TESSERACT_PATH

class OCRProcessor:
    def __init__(self):
        self.ocr_cache = {}
        self._load_cached_ocr()
    
    def _load_cached_ocr(self):
        if os.path.exists(OCR_PATH):
            try:
                with open(OCR_PATH, 'r', encoding='utf-8') as f:
                    self.ocr_cache = json.load(f)
            except Exception as e:
                print(f"⚠️  Impossible de charger le cache OCR: {e}")
    
    def run_ocr(self, image_path):
        filename = os.path.basename(image_path)
        
        # Vérifier le cache
        if filename in self.ocr_cache:
            return self.ocr_cache[filename]
        
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, lang=OCR_LANGUAGE)
            
            # Nettoyage du texte
            text = text.strip()
            if not text:
                text = "Aucun texte détecté"
            
            # Mise en cache
            self.ocr_cache[filename] = text
            
            print(f"  ✓ OCR effectué: {filename}")
            return text
        
        except pytesseract.TesseractNotFoundError:
            print(f"❌ Tesseract n'est pas installé. Installez-le et configurez TESSERACT_PATH")
            return "Erreur: Tesseract non disponible"
        
        except Exception as e:
            print(f"⚠️  Erreur OCR sur {filename}: {e}")
            return f"Erreur OCR: {str(e)}"
    
    def save_ocr_results(self):
        """Sauvegarde les résultats OCR dans un fichier JSON."""
        try:
            with open(OCR_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.ocr_cache, f, indent=2, ensure_ascii=False)
            print(f"✅ Résultats OCR sauvegardés: {OCR_PATH}")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde OCR: {e}")


# Instance globale
ocr_processor = OCRProcessor()

def run_ocr(image_path):
    """Fonction de compatibilité."""
    return ocr_processor.run_ocr(image_path)

def save_ocr_results():
    """Sauvegarde tous les résultats OCR."""
    ocr_processor.save_ocr_results()