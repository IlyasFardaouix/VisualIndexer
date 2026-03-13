"""
Photothèque Intelligente - Pipeline principal
Traitement complet des images: ingestion, OCR, tags, embeddings
"""

import os
import sys
import argparse
from datetime import datetime

from scripts.ingest import image_ingestor
from scripts.extract_metadata import metadata_extractor
from scripts.tag_clip import clip_tagger
from scripts.ocr import ocr_processor
from scripts.embeddings import embedding_manager
from config.settings import IMAGE_DIR, PROCESSED_IMAGE_DIR, EMBEDDING_PATH

def print_banner():
    print("\n=== PHOTOTHÈQUE INTELLIGENTE ===\n")

def print_section(title):
    print(f"\n--- {title} ---\n")

def run_pipeline():
    print_banner()
    
    if not os.path.exists(IMAGE_DIR) or not os.listdir(IMAGE_DIR):
        print(f"Pas d'images dans: {IMAGE_DIR}")
        return False
    
    try:
        # ÉTAPE 1: Ingestion
        print_section("📥 ÉTAPE 1: Ingestion des images")
        image_ingestor.ingest_images(IMAGE_DIR)
        stats = image_ingestor.get_statistics()
        print(f"\n✅ Ingestion terminée:")
        print(f"   • Images traitées: {stats['total_processed']}")
        print(f"   • Doublons trouvés: {stats['duplicates_found']}")
        
        # ÉTAPE 2: Métadonnées
        print_section("🔍 ÉTAPE 2: Extraction des métadonnées")
        metadata_extractor.save_metadata(PROCESSED_IMAGE_DIR)
        
        # ÉTAPE 3: OCR
        print_section("📄 ÉTAPE 3: Reconnaissance Optique de Caractères (OCR)")
        print("Extraction du texte des images...\n")
        
        # ÉTAPE 4: Tagging
        print_section("🏷️  ÉTAPE 4: Tagging automatique")
        print("Génération des tags...\n")
        
        # ÉTAPE 5: Embeddings
        print_section("🧠 ÉTAPE 5: Génération des vecteurs")
        print("Création des représentations vectorielles...\n")
        
        embeddings_dict = {}
        images_to_process = [
            f for f in os.listdir(PROCESSED_IMAGE_DIR)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
        ]
        
        for idx, filename in enumerate(images_to_process, 1):
            print(f"  [{idx}/{len(images_to_process)}] Traitement: {filename}")
            
            image_path = os.path.join(PROCESSED_IMAGE_DIR, filename)
            
            try:
                # OCR
                text = ocr_processor.run_ocr(image_path)
                
                # Tags CLIP
                tags = clip_tagger.get_clip_tags(image_path, top_k=5)
                
                # Combinaison texte + tags
                caption = f"{text} {' '.join(tags)}"
                
                # Embedding
                embedding = embedding_manager.generate_embedding(caption)
                if embedding:
                    embeddings_dict[filename] = embedding
                    print(f"      ✅ Traité avec succès")
                else:
                    print(f"      ⚠️  Embedding échoué")
                    
            except Exception as e:
                print(f"      ❌ Erreur: {str(e)[:50]}")
        
        # Sauvegarder les embeddings
        embedding_manager.store_embeddings(embeddings_dict)
        ocr_processor.save_ocr_results()
        
        # RÉSUMÉ FINAL
        print_section("✅ RÉSUMÉ FINAL")
        print(f"✓ Pipeline complété avec succès!")
        print(f"\n📊 Statistiques:")
        print(f"   • Images ingérées: {len(images_to_process)}")
        print(f"   • Embeddings générés: {len(embeddings_dict)}")
        print(f"   • OCR résultats: {len(ocr_processor.ocr_cache)}")
        print(f"\n💾 Fichiers de sortie:")
        print(f"   • Métadonnées: data/metadata.csv")
        print(f"   • Embeddings: data/embeddings.json")
        print(f"   • OCR: data/ocr_results.json")
        print(f"\n🚀 Prochaine étape:")
        print(f"   Lancez l'interface: streamlit run ui/interface.py")
        print(f"\n⏰ Fin: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_ui():
    print_banner()
    print("Démarrage de l'interface...\n")
    
    try:
        import subprocess
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run',
            'ui/interface.py',
            '--logger.level=warning'
        ])
    except ImportError:
        print("Streamlit n'est pas installé")
    except Exception as e:
        print(f"Erreur: {e}")

def run_ingest_only():
    print_banner()
    print_section("INGESTION UNIQUEMENT")
    image_ingestor.ingest_images(IMAGE_DIR)

def main():
    parser = argparse.ArgumentParser(description="Photothèque Intelligente")
    parser.add_argument('--mode', choices=['pipeline', 'ui', 'ingest'], default='pipeline',
                        help='Mode d\'exécution')
    args = parser.parse_args()
    
    if args.mode == 'pipeline':
        success = run_pipeline()
        sys.exit(0 if success else 1)
    elif args.mode == 'ui':
        run_ui()
    elif args.mode == 'ingest':
        run_ingest_only()

if __name__ == "__main__":
    main()