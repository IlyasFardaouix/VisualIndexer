import os
import csv
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from config.settings import IMAGE_DIR, PROCESSED_IMAGE_DIR, METADATA_PATH

class MetadataExtractor:
    
    def __init__(self):
        """Initialise l'extracteur."""
        self.metadata = []
    
    def extract_exif_data(self, image_path):
        """
        Extrait les données EXIF d'une image.
        
        Args:
            image_path (str): Chemin de l'image
            
        Returns:
            dict: Dictionnaire des données EXIF
        """
        exif_data = {}
        try:
            image = Image.open(image_path)
            exifdata = image.getexif()
            
            for tag_id, value in exifdata.items():
                tag_name = TAGS.get(tag_id, tag_id)
                try:
                    exif_data[tag_name] = str(value)[:100]  # Limiter la longueur
                except:
                    pass
        except Exception as e:
            print(f"⚠️  Impossible d'extraire EXIF de {image_path}: {e}")
        
        return exif_data
    
    def extract_image_info(self, image_path):
        """
        Extrait les informations générales d'une image.
        
        Args:
            image_path (str): Chemin de l'image
            
        Returns:
            dict: Dictionnaire avec les informations
        """
        info = {
            'filename': os.path.basename(image_path),
            'filepath': image_path,
            'size_kb': os.path.getsize(image_path) / 1024,
            'extracted_at': datetime.now().isoformat()
        }
        
        try:
            image = Image.open(image_path)
            info['width'] = image.width
            info['height'] = image.height
            info['format'] = image.format
            info['mode'] = image.mode
        except Exception as e:
            print(f"❌ Erreur lors de la lecture de {image_path}: {e}")
        
        return info
    
    def save_metadata(self, image_folder=IMAGE_DIR):
        """
        Extrait et sauvegarde les métadonnées de toutes les images.
        
        Args:
            image_folder (str): Dossier contenant les images
        """
        metadata_list = []
        
        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                image_path = os.path.join(image_folder, filename)
                
                info = self.extract_image_info(image_path)
                exif = self.extract_exif_data(image_path)
                info.update(exif)
                
                metadata_list.append(info)
                print(f"  ✓ Métadonnées extraites: {filename}")
        
        # Sauvegarde en CSV
        if metadata_list:
            try:
                keys = set()
                for item in metadata_list:
                    keys.update(item.keys())
                keys = sorted(list(keys))
                
                with open(METADATA_PATH, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(metadata_list)
                
                print(f"✅ Métadonnées sauvegardées: {METADATA_PATH}")
            except Exception as e:
                print(f"❌ Erreur lors de la sauvegarde: {e}")
        else:
            print("⚠️  Aucune image trouvée pour extraire les métadonnées")


# Instance globale
metadata_extractor = MetadataExtractor()

def save_metadata():
    """Fonction de compatibilité."""
    metadata_extractor.save_metadata()

def extract_metadata(image_path):
    """Extrait les métadonnées d'une seule image."""
    return metadata_extractor.extract_image_info(image_path)