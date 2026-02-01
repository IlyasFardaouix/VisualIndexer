#!/usr/bin/env pwsh
# Script pour faire les commits de manière organisée
# Usage: .\commit_all.ps1

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Phototheque Intelligente - Git Setup" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$commits = @(
    @{
        step = 1
        desc = "Configuration et dependencies"
        files = @("config/settings.py", ".env", "requirements.txt", ".gitignore")
        msg = "Initial: Configuration et dependencies"
    },
    @{
        step = 2
        desc = "Module d'ingestion"
        files = @("scripts/ingest.py")
        msg = "Feature: Ingestion images et detection doublons"
    },
    @{
        step = 3
        desc = "Module métadonnées"
        files = @("scripts/extract_metadata.py")
        msg = "Feature: Extraction metadonnees et EXIF"
    },
    @{
        step = 4
        desc = "Module OCR"
        files = @("scripts/ocr.py")
        msg = "Feature: OCR et reconnaissance texte"
    },
    @{
        step = 5
        desc = "Module tagging"
        files = @("scripts/tag_clip.py")
        msg = "Feature: Tagging automatique avec CLIP"
    },
    @{
        step = 6
        desc = "Embeddings et recherche"
        files = @("scripts/embeddings.py", "scripts/search.py")
        msg = "Feature: Embeddings et moteur de recherche"
    },
    @{
        step = 7
        desc = "Interface utilisateur"
        files = @("ui/")
        msg = "Feature: Interface Streamlit"
    },
    @{
        step = 8
        desc = "Pipeline principal"
        files = @("main.py", "scripts/__init__.py", "ui/__init__.py")
        msg = "Core: Pipeline orchestrateur principal"
    },
    @{
        step = 9
        desc = "Documentation et outils"
        files = @("README.md", "GUIDE_UTILISATION.md", "INSTALLATION.md", "tools/")
        msg = "Docs: Documentation et outils"
    }
)

foreach ($commit in $commits) {
    Write-Host "[{0}/9] {1}..." -f $commit.step, $commit.desc -ForegroundColor Yellow
    
    # Ajouter les fichiers
    foreach ($file in $commit.files) {
        git add $file
    }
    
    # Créer le commit
    git commit -m $commit.msg
    Write-Host "✓ Commit: $($commit.msg)" -ForegroundColor Green
    Write-Host ""
}

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Commits crees avec succes!" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Etapes suivantes:" -ForegroundColor Yellow
Write-Host "1. Creer un repo sur GitHub: ilyasFardaouix/phototheque_intelligente"
Write-Host "2. Executer: git remote add origin https://github.com/ilyasFardaouix/phototheque_intelligente.git"
Write-Host "3. Executer: git push -u origin main"
Write-Host ""

Write-Host "Historique des commits:" -ForegroundColor Cyan
git log --oneline
Write-Host ""
