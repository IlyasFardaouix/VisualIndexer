"""
Module de tagging automatique utilisant CLIP.
Génère automatiquement des tags pertinents pour chaque image.
"""

import os
import json
from PIL import Image
import torch

try:
    from transformers import CLIPProcessor, CLIPModel
except ImportError:
    print(
        "⚠️  Transformers n'est pas installé. Installez avec: pip install transformers"
    )

from config.settings import MODEL_CACHE_DIR, CLIP_MODEL


class CLIPTagger:
    """Générateur de tags automatiques utilisant CLIP."""

    def __init__(self):
        """Initialise le modèle CLIP."""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🚀 Utilisation du device: {self.device}")

        try:
            self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
            self.processor = CLIPProcessor.from_pretrained(
                "openai/clip-vit-base-patch32"
            )
            self.model = self.model.to(self.device)
        except Exception as e:
            print(f"⚠️  Erreur lors du chargement de CLIP: {e}")
            self.model = None
            self.processor = None

        # Prédéfini de tags possibles
        self.candidate_tags = [
            "personne",
            "visage",
            "paysage",
            "montagne",
            "mer",
            "forêt",
            "ville",
            "urbain",
            "bâtiment",
            "architecture",
            "nature",
            "animal",
            "chien",
            "chat",
            "oiseau",
            "insecte",
            "voiture",
            "route",
            "fleur",
            "arbre",
            "eau",
            "intérieur",
            "extérieur",
            "jour",
            "nuit",
            "coucher de soleil",
            "portrait",
            "groupe",
            "selfie",
            "nourriture",
            "boisson",
            "texte",
            "document",
            "écran",
            "espace",
            "abstrait",
            "noir et blanc",
            "couleur",
            "vintage",
            "moderne",
            "flou",
        ]

    def get_clip_tags(self, image_path, top_k=5):
        """
        Génère des tags automatiques pour une image.

        Args:
            image_path (str): Chemin de l'image
            top_k (int): Nombre de tags à générer

        Returns:
            list: Liste des tags pertinents
        """
        if not self.model or not self.processor:
            print(f"⚠️  Modèle CLIP non disponible pour {image_path}")
            return ["sans-tag"]

        try:
            # Charger et pré-traiter l'image
            image = Image.open(image_path).convert("RGB")

            # Préparer les inputs
            inputs = self.processor(
                text=self.candidate_tags,
                images=image,
                return_tensors="pt",
                padding=True,
            )
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # Générer les probabilités
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits_per_image = outputs.logits_per_image

            # Extraire les meilleurs tags
            probs = logits_per_image.softmax(dim=1)[0]
            top_indices = torch.topk(probs, top_k).indices.cpu().numpy()

            tags = [self.candidate_tags[idx] for idx in top_indices]
            print(f"  ✓ Tags générés: {image_path}")
            return tags

        except Exception as e:
            print(f"⚠️  Erreur lors du tagging de {image_path}: {e}")
            return ["erreur-tagging"]

    def tag_batch(self, image_paths):
        """
        Génère des tags pour plusieurs images.

        Args:
            image_paths (list): Liste des chemins d'images

        Returns:
            dict: Dictionnaire {filename: tags}
        """
        results = {}
        for image_path in image_paths:
            filename = os.path.basename(image_path)
            tags = self.get_clip_tags(image_path)
            results[filename] = tags

        return results


# Instance globale
clip_tagger = CLIPTagger()


def get_clip_tags(image_path, top_k=5):
    """Fonction de compatibilité."""
    return clip_tagger.get_clip_tags(image_path, top_k)


def tag_batch(image_paths):
    """Génère des tags en batch."""
    return clip_tagger.tag_batch(image_paths)
