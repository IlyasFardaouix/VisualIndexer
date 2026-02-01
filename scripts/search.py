"""
Module de recherche avancée dans la photothèque.
Permet de rechercher les images par texte, tags, métadonnées et similarité.
"""
import csv
import os
from scripts.embeddings import embedding_manager
from config.settings import METADATA_PATH

class ImageSearchEngine:
    """Moteur de recherche pour la photothèque."""
    
    def __init__(self):
        """Initialise le moteur de recherche."""
        self.metadata = self._load_metadata()
    
    def _load_metadata(self):
        """Charge les métadonnées depuis le fichier CSV."""
        metadata = {}
        if os.path.exists(METADATA_PATH):
            try:
                with open(METADATA_PATH, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        filename = row.get('filename')
                        if filename:
                            metadata[filename] = row
            except Exception as e:
                print(f"⚠️  Erreur lors du chargement des métadonnées: {e}")
        return metadata
    
    def search_by_text(self, query, top_k=10):
        """
        Recherche par texte utilisant les embeddings.
        
        Args:
            query (str): Requête textuelle
            top_k (int): Nombre de résultats
            
        Returns:
            list: Résultats avec scores de similarité
        """
        results = embedding_manager.search_similar(query, top_k)
        return results
    
    def search_by_metadata(self, filters):
        """
        Recherche par métadonnées.
        
        Args:
            filters (dict): Critères de recherche
                {
                    'min_width': 800,
                    'min_height': 600,
                    'format': 'JPEG'
                }
        
        Returns:
            list: Fichiers correspondant aux critères
        """
        results = []
        
        for filename, metadata in self.metadata.items():
            match = True
            
            for key, value in filters.items():
                if key == 'min_width':
                    if int(metadata.get('width', 0)) < value:
                        match = False
                        break
                elif key == 'min_height':
                    if int(metadata.get('height', 0)) < value:
                        match = False
                        break
                elif key == 'format':
                    if metadata.get('format', '').upper() != value.upper():
                        match = False
                        break
                elif key in metadata:
                    if metadata[key] != value:
                        match = False
                        break
            
            if match:
                results.append(filename)
        
        return results
    
    def search_by_tags(self, tags, mode='any'):
        """
        Recherche par tags (nécessite les tags générés préalablement).
        
        Args:
            tags (list): Tags à chercher
            mode (str): 'any' ou 'all'
        
        Returns:
            list: Fichiers correspondant
        """
        # Note: Nécessite une table tags en base de données
        # Implémentation future avec persistance des tags
        return []
    
    def advanced_search(self, text_query=None, metadata_filters=None, limit=20):
        """
        Recherche avancée combinée.
        
        Args:
            text_query (str): Requête textuelle
            metadata_filters (dict): Filtres sur les métadonnées
            limit (int): Nombre max de résultats
        
        Returns:
            list: Résultats combinés
        """
        results = []
        
        if text_query:
            text_results = self.search_by_text(text_query, top_k=limit)
            for filename, score in text_results:
                results.append({
                    'filename': filename,
                    'score': score,
                    'source': 'text'
                })
        
        if metadata_filters:
            metadata_results = self.search_by_metadata(metadata_filters)
            for filename in metadata_results:
                # Vérifier si déjà dans les résultats
                if not any(r['filename'] == filename for r in results):
                    results.append({
                        'filename': filename,
                        'score': 0.5,
                        'source': 'metadata'
                    })
        
        return results[:limit]
    
    def get_image_info(self, filename):
        """
        Récupère les informations complètes d'une image.
        
        Args:
            filename (str): Nom du fichier
        
        Returns:
            dict: Informations de l'image
        """
        return self.metadata.get(filename, {})


# Instance globale
search_engine = ImageSearchEngine()

def search_by_text(query, top_k=10):
    """Fonction de compatibilité."""
    return search_engine.search_by_text(query, top_k)

def search_by_metadata(filters):
    """Fonction de compatibilité."""
    return search_engine.search_by_metadata(filters)

def advanced_search(text_query=None, metadata_filters=None, limit=20):
    """Fonction de compatibilité."""
    return search_engine.advanced_search(text_query, metadata_filters, limit)