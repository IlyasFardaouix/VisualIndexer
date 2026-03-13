import pytest
from unittest.mock import Mock, patch
from your_module import run_pipeline, run_ui, run_ingest_only, main

def test_print_banner():
    """Teste la fonction print_banner."""
    with patch('builtins.print') as mock_print:
        run_pipeline()
        mock_print.assert_called_once_with("\n=== PHOTOTHÈQUE INTELLIGENTE ===\n")

def test_print_section():
    """Teste la fonction print_section."""
    with patch('builtins.print') as mock_print:
        run_pipeline()
        mock_print.assert_any_call("\n--- ÉTAPE 1: Ingestion des images ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 2: Extraction des métadonnées ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 3: Reconnaissance Optique de Caractères (OCR) ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 4: Tagging automatique ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 5: Génération des vecteurs ---\n")
        mock_print.assert_any_call("\n--- RÉSUMÉ FINAL ---\n")

def test_run_pipeline():
    """Teste la fonction run_pipeline."""
    with patch('os.path.exists') as mock_exists, patch('os.listdir') as mock_listdir, patch('builtins.print') as mock_print:
        mock_exists.return_value = True
        mock_listdir.return_value = ['image1.jpg', 'image2.jpg']
        run_pipeline()
        mock_print.assert_called_with("\n=== PHOTOTHÈQUE INTELLIGENTE ===\n")
        mock_print.assert_any_call("\n--- ÉTAPE 1: Ingestion des images ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 2: Extraction des métadonnées ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 3: Reconnaissance Optique de Caractères (OCR) ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 4: Tagging automatique ---\n")
        mock_print.assert_any_call("\n--- ÉTAPE 5: Génération des vecteurs ---\n")
        mock_print.assert_any_call("\n--- RÉSUMÉ FINAL ---\n")
        mock_print.assert_any_call("✓ Pipeline complété avec succès!")

def test_run_ui():
    """Teste la fonction run_ui."""
    with patch('builtins.print') as mock_print, patch('subprocess.run') as mock_subprocess:
        run_ui()
        mock_print.assert_called_once_with("\n=== PHOTOTHÈQUE INTELLIGENTE ===\n")
        mock_print.assert_any_call("Démarrage de l'interface...\n")
        mock_subprocess.assert_called_once_with([
            sys.executable, '-m', 'streamlit', 'run',
            'ui/interface.py',
            '--logger.level=warning'
        ])

def test_run_ingest_only():
    """Teste la fonction run_ingest_only."""
    with patch('builtins.print') as mock_print:
        run_ingest_only()
        mock_print.assert_called_once_with("\n=== PHOTOTHÈQUE INTELLIGENTE ===\n")
        mock_print.assert_any_call("\n--- INGESTION UNIQUEMENT ---\n")

def test_main():
    """Teste la fonction main."""
    with patch('argparse.ArgumentParser') as mock_argparse, patch('your_module.run_pipeline') as mock_run_pipeline, patch('your_module.run_ui') as mock_run_ui, patch('your_module.run_ingest_only') as mock_run_ingest_only:
        mock_argparse.return_value.parse_args.return_value.mode = 'pipeline'
        main()
        mock_run_pipeline.assert_called_once()
        mock_argparse.return_value.parse_args.return_value.mode = 'ui'
        main()
        mock_run_ui.assert_called_once()
        mock_argparse.return_value.parse_args.return_value.mode = 'ingest'
        main()
        mock_run_ingest_only.assert_called_once()

def test_main_invalid_mode():
    """Teste la fonction main avec un mode non valide."""
    with patch('argparse.ArgumentParser') as mock_argparse, patch('builtins.print') as mock_print:
        mock_argparse.return_value.parse_args.return_value.mode = 'invalid'
        main()
        mock_print.assert_called_once_with("Error: invalid choice: 'invalid' (choose from 'pipeline', 'ui', 'ingest')")

def test_main_no_mode():
    """Teste la fonction main sans mode."""
    with patch('argparse.ArgumentParser') as mock_argparse, patch('builtins.print') as mock_print:
        mock_argparse.return_value.parse_args.return_value.mode = None
        main()
        mock_print.assert_called_once_with("Error: mode is required")

def test_main_no_streamlit():
    """Teste la fonction main sans Streamlit."""
    with patch('builtins.print') as mock_print, patch('subprocess.run') as mock_subprocess:
        mock_subprocess.side_effect = ImportError
        run_ui()
        mock_print.assert_called_once_with("Streamlit n'est pas installé")

def test_main_invalid_streamlit():
    """Teste la fonction main avec un Streamlit non valide."""
    with patch('builtins.print') as mock_print, patch('subprocess.run') as mock_subprocess:
        mock_subprocess.side_effect = Exception
        run_ui()
        mock_print.assert_called_once_with("Erreur: <Exception>")

def test_main_invalid_ingest():
    """Teste la fonction main avec une ingestion non valide."""
    with patch('builtins.print') as mock_print, patch('your_module.ImageIngestor.ingest_images') as mock_ingest_images:
        mock_ingest_images.side_effect = Exception
        run_ingest_only()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")

def test_main_invalid_ocr():
    """Teste la fonction main avec un OCR non valide."""
    with patch('builtins.print') as mock_print, patch('your_module.OcrProcessor.run_ocr') as mock_run_ocr:
        mock_run_ocr.side_effect = Exception
        run_pipeline()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")

def test_main_invalid_tagging():
    """Teste la fonction main avec un tagging non valide."""
    with patch('builtins.print') as mock_print, patch('your_module.ClipTagger.get_clip_tags') as mock_get_clip_tags:
        mock_get_clip_tags.side_effect = Exception
        run_pipeline()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")

def test_main_invalid_embeddings():
    """Teste la fonction main avec des embeddings non valides."""
    with patch('builtins.print') as mock_print, patch('your_module.EmbeddingManager.generate_embedding') as mock_generate_embedding:
        mock_generate_embedding.side_effect = Exception
        run_pipeline()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")

def test_main_invalid_save_embeddings():
    """Teste la fonction main avec un sauvegardage d'embeddings non valide."""
    with patch('builtins.print') as mock_print, patch('your_module.EmbeddingManager.store_embeddings') as mock_store_embeddings:
        mock_store_embeddings.side_effect = Exception
        run_pipeline()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")

def test_main_invalid_save_ocr():
    """Teste la fonction main avec un sauvegardage d'OCR non valide."""
    with patch('builtins.print') as mock_print, patch('your_module.OcrProcessor.save_ocr_results') as mock_save_ocr_results:
        mock_save_ocr_results.side_effect = Exception
        run_pipeline()
        mock_print.assert_called_once_with("❌ Erreur: <Exception>")