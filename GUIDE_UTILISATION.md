# Guide d'Utilisation - Photothèque Intelligente

## Démarrage Rapide

### 1. Préparation des images

Placez vos images dans ce dossier:
```
data/images/raw/
```

Types d'images supportées:
- JPG, JPEG (photos standards)
- PNG (avec transparence)
- GIF (animations)
- WebP (modernes)
- BMP (bitmap)

### 2. Ingestion des images

Lancez l'ingestion pour optimiser et analyser les images:

```bash
python main.py --mode ingest
```

Cela va:
- Détecter les doublons
- Compresser les images
- Redimensionner si nécessaire
- Extraire les métadonnées
- Générer les embeddings

### 3. Lancer l'interface

Une fois l'ingestion terminée, lancez l'interface web:

```bash
python main.py --mode ui
```

Puis ouvrez votre navigateur sur: **http://localhost:8501**

---

## Modes d'Utilisation

### Mode Ingestion
```bash
python main.py --mode ingest
```
✓ Traite les images du dossier `data/images/raw/`
✓ Génère les fichiers de sortie

### Mode Pipeline Complet
```bash
python main.py --mode pipeline
```
✓ Fait l'ingestion
✓ Génère métadonnées
✓ Exécute l'OCR
✓ Génère les tags
✓ Crée les embeddings
⏱️ Prend du temps (charge les modèles IA)

### Mode Interface
```bash
python main.py --mode ui
```
✓ Lance le dashboard interactif
✓ Recherche images
✓ Visualise les galeries
✓ Explore les métadonnées

---

## Utilisation de l'Interface

### Page d'Accueil
- Statistiques globales
- Nombre d'images
- Embeddings indexés
- À propos du projet

### Recherche
- **Recherche texte** - Trouve des images par description
- **Filtrage métadonnées** - Par dimensions, format, etc.
- **Recherche combinée** - Combine texte + filtres

Exemple de recherche:
```
"paysage montagne"
"coucher de soleil"
"groupe de personnes"
"document texte"
```

### Galerie
- Visualise toutes les images
- Ajuste le nombre de colonnes
- Voir les détails de chaque image

### Détails
- Informations complètes d'une image
- Métadonnées EXIF
- Texte OCR
- Tags générés

---

## Fichiers de Sortie

Après traitement, trouvez:

| Fichier | Contenu |
|---|---|
| `data/metadata.csv` | Métadonnées (EXIF, dimensions, etc.) |
| `data/embeddings.json` | Vecteurs pour recherche |
| `data/ocr_results.json` | Texte extrait des images |
| `data/images/processed/` | Images optimisées |

---

## Configuration Avancée

Fichier `.env`:
```
# Chemin Tesseract OCR (pour reconnaissance texte)
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# Langue OCR (fra = français, eng = anglais)
OCR_LANGUAGE=fra+eng

# Qualité de compression JPEG (0-100)
IMAGE_QUALITY=85

# Taille batch pour traitement
BATCH_SIZE=32

# Dimensions max des images
# MAX_IMAGE_SIZE=1920x1080
```

---

## Troubleshooting

### Erreur: "Tesseract not found"
Pour utiliser l'OCR, installez Tesseract:
- Windows: https://github.com/tesseract-ocr/tesseract/wiki/Downloads
- Linux: `sudo apt install tesseract-ocr`
- Mac: `brew install tesseract`

Puis mettez à jour `.env` avec le chemin correct.

### Erreur: "No module named ..."
Réinstallez les dépendances:
```bash
pip install -r requirements.txt
```

### L'ingestion est lente
- C'est normal pour la première fois (téléchargement modèles IA)
- Les fois suivantes seront plus rapides (cache)
- Patience pour 100+ images

### Streamlit ne démarre pas
Vérifiez le port 8501 est libre:
```bash
# Linux/Mac
lsof -i :8501

# Windows
netstat -ano | findstr :8501
```

---

## Conseils d'Utilisation

✓ **Pour commencer**: 5-10 images pour tester
✓ **Formats optimaux**: JPG pour photos, PNG pour graphiques
✓ **Nommage**: Utilisez des noms descriptifs
✓ **OCR**: Le français + anglais fonctionne mieux
✓ **Recherche**: Décrivez ce que vous cherchez naturellement

---

## Performance

| Opération | Temps | Notes |
|---|---|---|
| Ingestion 10 images | ~10s | Dépend taille |
| OCR 1 image | ~1-2s | Premiers appels lents |
| Tagging CLIP | ~2-3s | Charge modèle |
| Recherche | <100ms | Très rapide |

---

## Support

Pour des questions ou problèmes:
1. Vérifiez les logs dans la console
2. Consultez la documentation des packages (PIL, Streamlit, Transformers)
3. Vérifiez la configuration `.env`
4. Relancez l'ingestion complète

---

**Bon usage de votre Photothèque !** 📸
