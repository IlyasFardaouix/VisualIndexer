import json
import numpy as np
from sentence_transformers import SentenceTransformer
from config.settings import EMBEDDING_MODEL, EMBEDDING_PATH, MODEL_CACHE_DIR
import os

class EmbeddingManager:
    def __init__(self):
        self.model = SentenceTransformer(
            EMBEDDING_MODEL,
            cache_folder=MODEL_CACHE_DIR
        )
        self.embeddings_cache = {}
        self._load_existing_embeddings()
    def _load_existing_embeddings(self):
        if os.path.exists(EMBEDDING_PATH):
            try:
                with open(EMBEDDING_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.embeddings_cache = data
            except Exception as e:
                print(f"⚠️  Impossible de charger les embeddings: {e}")
    
    def generate_embedding(self, text):
        try:
            embedding = self.model.encode(text, convert_to_numpy=True)
            return embedding.tolist()
        except Exception as e:
            print(f"Erreur embedding: {e}")
            return None
    
    def store_embeddings(self, embeddings_dict):
        try:
            self.embeddings_cache.update(embeddings_dict)
            with open(EMBEDDING_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.embeddings_cache, f, indent=2)
            print(f"✅ {len(embeddings_dict)} embeddings sauvegardés")
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
    
    def search_similar(self, query_text, top_k=5):
        if not self.embeddings_cache:
            return []
        
        query_embedding = np.array(self.generate_embedding(query_text))
        similarities = {}
        
        for filename, emb in self.embeddings_cache.items():
            emb_array = np.array(emb)
            # Calcul de la similarité cosinus
            similarity = np.dot(query_embedding, emb_array) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(emb_array) + 1e-8
            )
            similarities[filename] = float(similarity)
        
        sorted_results = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_results[:top_k]


# Instance globale
embedding_manager = EmbeddingManager()

def generate_embedding(text):
    """Fonction de compatibilité."""
    return embedding_manager.generate_embedding(text)

def store_embeddings(embeddings_dict):
    """Fonction de compatibilité."""
    embedding_manager.store_embeddings(embeddings_dict)

def search_similar(query_text, top_k=5):
    """Fonction de compatibilité."""
    return embedding_manager.search_similar(query_text, top_k)