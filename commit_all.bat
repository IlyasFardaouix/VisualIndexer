@echo off
REM Script pour faire les commits de manière organisée
REM Usage: commit_all.bat

echo.
echo ===================================
echo Phototheque Intelligente - Git Setup
echo ===================================
echo.

REM Commit 1: Configuration
echo [1/9] Configuration et dependencies...
git add config/settings.py .env requirements.txt .gitignore
git commit -m "Initial: Configuration et dependencies"

REM Commit 2: Ingestion
echo [2/9] Module d'ingestion...
git add scripts/ingest.py
git commit -m "Feature: Ingestion images et detection doublons"

REM Commit 3: Métadonnées
echo [3/9] Module métadonnées...
git add scripts/extract_metadata.py
git commit -m "Feature: Extraction metadonnees et EXIF"

REM Commit 4: OCR
echo [4/9] Module OCR...
git add scripts/ocr.py
git commit -m "Feature: OCR et reconnaissance texte"

REM Commit 5: Tagging
echo [5/9] Module tagging...
git add scripts/tag_clip.py
git commit -m "Feature: Tagging automatique avec CLIP"

REM Commit 6: Embeddings et Recherche
echo [6/9] Embeddings et recherche...
git add scripts/embeddings.py scripts/search.py
git commit -m "Feature: Embeddings et moteur de recherche"

REM Commit 7: Interface
echo [7/9] Interface utilisateur...
git add ui/
git commit -m "Feature: Interface Streamlit"

REM Commit 8: Pipeline
echo [8/9] Pipeline principal...
git add main.py scripts/__init__.py ui/__init__.py
git commit -m "Core: Pipeline orchestrateur principal"

REM Commit 9: Documentation
echo [9/9] Documentation et outils...
git add README.md GUIDE_UTILISATION.md INSTALLATION.md tools/
git commit -m "Docs: Documentation et outils"

echo.
echo ===================================
echo Commits crees avec succes!
echo ===================================
echo.
echo Etapes suivantes:
echo 1. Creer un repo sur GitHub: ilyasFardaouix/phototheque_intelligente
echo 2. Executer: git remote add origin https://github.com/ilyasFardaouix/phototheque_intelligente.git
echo 3. Executer: git push -u origin main
echo.
git log --oneline
echo.
