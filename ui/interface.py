import streamlit as st
import os
from PIL import Image
import pandas as pd
from datetime import datetime
from scripts.search import search_engine
from scripts.embeddings import embedding_manager
from config.settings import PROCESSED_IMAGE_DIR, IMAGE_DIR

st.set_page_config(page_title="Photothèque Intelligente", page_icon="📸", layout="wide")


def get_all_images():
    """Récupère toutes les images du dossier processed."""
    images = []
    if os.path.exists(PROCESSED_IMAGE_DIR):
        for filename in os.listdir(PROCESSED_IMAGE_DIR):
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
                images.append(filename)
    return sorted(images)


def display_image_grid(images, cols=3):
    """Affiche les images dans une grille."""
    if not images:
        st.info("Aucune image à afficher.")
        return

    cols_list = st.columns(cols)
    for idx, image_file in enumerate(images):
        col = cols_list[idx % cols]
        image_path = os.path.join(PROCESSED_IMAGE_DIR, image_file)

        try:
            img = Image.open(image_path)
            with col:
                st.image(img, caption=image_file, use_column_width=True)
                if st.button(f"Voir détails", key=f"btn_{idx}"):
                    st.session_state.selected_image = image_file
        except Exception as e:
            st.error(f"Erreur avec {image_file}: {e}")


def main():
    """Fonction principale de l'application."""

    # En-tête
    st.title("📸 Photothèque Intelligente")
    st.markdown("**Exploration et recherche intelligente de vos images avec IA**")
    st.divider()

    # Barre latérale
    with st.sidebar:
        st.header("⚙️ Menu")
        page = st.radio(
            "Sélectionnez une page:",
            ["Accueil", "Recherche", "Galerie", "Détails", "Gestion"],
        )

    # Page: Accueil
    if page == "Accueil":
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Statistiques")
            images = get_all_images()
            st.metric("Images importées", len(images))
            st.metric("Embeddings indexés", len(embedding_manager.embeddings_cache))

        with col2:
            st.subheader("ℹ️ À propos")
            st.markdown("""
            La **Photothèque Intelligente** est un système de gestion et recherche 
            d'images alimenté par l'IA.
            
            **Fonctionnalités:**
            - 🔍 Recherche par texte avec similarité
            - 🏷️ Tagging automatique
            - 📝 OCR et extraction de métadonnées
            - 💾 Optimisation et stockage intelligent
            """)

    # Page: Recherche
    elif page == "Recherche":
        st.subheader("🔍 Recherche Avancée")

        search_tab1, search_tab2, search_tab3 = st.tabs(
            ["Texte", "Métadonnées", "Combinée"]
        )

        with search_tab1:
            st.markdown("**Recherche par texte avec similarité**")
            query = st.text_input(
                "Entrez votre requête:", placeholder="Ex: paysage montagne"
            )
            num_results = st.slider("Nombre de résultats", 1, 20, 5)

            if st.button("🔎 Rechercher"):
                if query:
                    with st.spinner("Recherche en cours..."):
                        results = search_engine.search_by_text(query, num_results)

                        if results:
                            st.success(f"✅ {len(results)} résultat(s) trouvé(s)")

                            # Afficher les résultats
                            for idx, (filename, score) in enumerate(results):
                                col1, col2 = st.columns([3, 1])

                                image_path = os.path.join(PROCESSED_IMAGE_DIR, filename)
                                if os.path.exists(image_path):
                                    with col1:
                                        img = Image.open(image_path)
                                        st.image(
                                            img, caption=filename, use_column_width=True
                                        )
                                    with col2:
                                        st.metric("Score", f"{score:.2%}")
                        else:
                            st.warning("Aucun résultat trouvé.")

        with search_tab2:
            st.markdown("**Recherche par critères de métadonnées**")

            col1, col2 = st.columns(2)
            with col1:
                min_width = st.number_input("Largeur minimale (px)", value=0)
                min_height = st.number_input("Hauteur minimale (px)", value=0)

            with col2:
                img_format = st.selectbox("Format", ["Tous", "JPEG", "PNG", "WEBP"])

            if st.button("🔎 Filtrer"):
                filters = {}
                if min_width > 0:
                    filters["min_width"] = min_width
                if min_height > 0:
                    filters["min_height"] = min_height
                if img_format != "Tous":
                    filters["format"] = img_format

                results = search_engine.search_by_metadata(filters)
                st.info(f"✅ {len(results)} image(s) correspond(ent)")

                if results:
                    display_image_grid(results)

        with search_tab3:
            st.markdown("**Recherche combinée (texte + métadonnées)**")
            query = st.text_input("Requête textuelle (optionnel):")
            min_width = st.number_input("Largeur min (px)", value=0, key="adv_width")

            if st.button("🔎 Recherche combinée"):
                filters = {"min_width": min_width} if min_width > 0 else None
                results = search_engine.advanced_search(query, filters)

                st.info(f"✅ {len(results)} résultat(s)")

    # Page: Galerie
    elif page == "Galerie":
        st.subheader("🖼️ Galerie")

        images = get_all_images()
        cols = st.slider("Colonnes", 1, 6, 3)

        if images:
            display_image_grid(images, cols=cols)
        else:
            st.info("Aucune image importée. Importez d'abord des images.")

    # Page: Détails
    elif page == "Détails":
        st.subheader("📋 Détails des Images")

        images = get_all_images()
        if images:
            selected = st.selectbox("Sélectionnez une image:", images)

            # Afficher l'image
            image_path = os.path.join(PROCESSED_IMAGE_DIR, selected)
            img = Image.open(image_path)

            col1, col2 = st.columns(2)

            with col1:
                st.image(img, use_column_width=True)

            with col2:
                st.markdown("**Informations**")
                metadata = search_engine.get_image_info(selected)

                if metadata:
                    st.write(
                        pd.DataFrame(
                            list(metadata.items()), columns=["Propriété", "Valeur"]
                        )
                    )
                else:
                    st.info("Pas de métadonnées disponibles.")
        else:
            st.info("Aucune image disponible.")

    # Page: Gestion
    elif page == "Gestion":
        st.subheader("⚙️ Gestion du Système")

        tab1, tab2 = st.tabs(["Informations", "Actions"])

        with tab1:
            images = get_all_images()

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📸 Images", len(images))
            with col2:
                st.metric("🗂️ Dossier", PROCESSED_IMAGE_DIR.split(os.sep)[-2:])
            with col3:
                st.metric("⏰ Mise à jour", datetime.now().strftime("%d/%m/%Y %H:%M"))

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Embeddings**")
                st.info(
                    f"✅ {len(embedding_manager.embeddings_cache)} embeddings indexés"
                )

            with col2:
                st.markdown("**Cache**")
                st.info(
                    f"🗂️ Taille du cache: {len(embedding_manager.embeddings_cache)} entrées"
                )

        with tab2:
            st.markdown("**Actions disponibles**")

            if st.button("🔄 Actualiser l'index"):
                with st.spinner("Actualisation en cours..."):
                    embedding_manager._load_existing_embeddings()
                    search_engine.metadata = search_engine._load_metadata()
                    st.success("✅ Index actualisé!")

            st.divider()

            if st.button("🗑️ Vider le cache"):
                if st.confirm("Êtes-vous sûr?"):
                    embedding_manager.embeddings_cache = {}
                    st.success("✅ Cache vidé!")


if __name__ == "__main__":
    main()
