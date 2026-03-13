import os
import hashlib
import shutil
from PIL import Image
from config.settings import IMAGE_DIR, PROCESSED_IMAGE_DIR, IMAGE_QUALITY, MAX_IMAGE_SIZE

class ImageIngestor:
    def __init__(self):
        self.processed_hashes = set()
        self.duplicates = []
    
    def hash_image(self, image_path):
        try:
            with open(image_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            print(f"⚠️  Erreur lors du hash de {image_path}: {e}")
            return None
    
    def optimize_image(self, input_path, output_path=None):
        """
        Optimise une image en réduisant sa taille et en compressant.
        
        Args:
            input_path (str): Chemin de l'image source
            output_path (str): Chemin de sortie (optionnel)
        
        Returns:
            bool: Succès de l'opération
        """
        if output_path is None:
            output_path = input_path
        
        try:
            image = Image.open(input_path)
            
            # Redimensionner si nécessaire
            if image.size[0] > MAX_IMAGE_SIZE[0] or image.size[1] > MAX_IMAGE_SIZE[1]:
                image.thumbnail(MAX_IMAGE_SIZE, Image.Resampling.LANCZOS)
            
            # Convertir en RGB si nécessaire
            if image.mode in ('RGBA', 'LA', 'P'):
                rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                image = rgb_image
            
            # Sauvegarder avec compression
            image.save(output_path, 'JPEG', quality=IMAGE_QUALITY, optimize=True)
            print(f"  ✓ Image optimisée: {os.path.basename(input_path)}")
            return True
        
        except Exception as e:
            print(f"⚠️  Erreur lors de l'optimisation de {input_path}: {e}")
            return False
    
    def ingest_images(self, source_folder=None, remove_duplicates=True):
        """
        Ingère les images d'un dossier.
        
        Args:
            source_folder (str): Dossier source (défaut: IMAGE_DIR)
            remove_duplicates (bool): Supprimer les doublons
        """
        if source_folder is None:
            source_folder = IMAGE_DIR
        
        if not os.path.exists(source_folder):
            print(f"⚠️  Dossier non trouvé: {source_folder}")
            return
        
        print(f"📁 Ingestion depuis: {source_folder}")
        
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')):
                source_path = os.path.join(source_folder, filename)
                output_path = os.path.join(PROCESSED_IMAGE_DIR, filename)
                
                # Calculer le hash
                img_hash = self.hash_image(source_path)
                if not img_hash:
                    continue
                
                # Vérifier les doublons
                if img_hash in self.processed_hashes:
                    print(f"[⚠️] Doublon détecté: {filename}")
                    self.duplicates.append(filename)
                    if remove_duplicates:
                        # Optionnel: déplacer vers un dossier duplicates
                        pass
                    continue
                
                # Ajouter au hash set
                self.processed_hashes.add(img_hash)
                
                # Optimiser et stocker
                if self.optimize_image(source_path, output_path):
                    print(f"[✓] Image importée: {filename}")
                else:
                    print(f"[✗] Erreur lors du traitement: {filename}")
        
        print(f"\n📊 Résumé de l'ingestion:")
        print(f"  ✓ Images traitées: {len(self.processed_hashes)}")
        print(f"  ⚠️  Doublons trouvés: {len(self.duplicates)}")
    
    def get_statistics(self):
        """Retourne les statistiques d'ingestion."""
        return {
            'total_processed': len(self.processed_hashes),
            'duplicates_found': len(self.duplicates),
            'processed_hashes': self.processed_hashes,
            'duplicates': self.duplicates
        }


# Instance globale
image_ingestor = ImageIngestor()

def ingest_images(folder=IMAGE_DIR):
    """Fonction de compatibilité."""
    image_ingestor.ingest_images(folder)

def hash_image(image_path):
    """Fonction de compatibilité."""
    return image_ingestor.hash_image(image_path)
