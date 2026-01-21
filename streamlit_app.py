
# Version 2025-12
## MAJ 2026-01-21 : Modifier pour avoir 2 colonnes sur android (CSS Grid personnalisé au lieu de st.columns)


import streamlit as st
import os

# 1. Configuration de la page (UNE SEULE FOIS)
st.set_page_config(page_title="NEXUS HUB", page_icon="💠", layout="wide")

# 2. Injection CSS pour FORCER le mode 2 colonnes sur Mobile
st.markdown("""
    <style>
    /* Force les colonnes à ne pas s'empiler sur mobile */
    [data-testid="column"] {
        width: 48% !important;
        flex: 1 1 48% !important;
        min-width: 48% !important;
    }
    
    /* Ajustement de l'espacement entre les colonnes */
    [data-testid="stHorizontalBlock"] {
        gap: 10px !important;
    }

    /* Style général */
    .main { background-color: #0F111A; }
    h1 { text-align: center; color: #51A8FF; font-family: 'Segoe UI'; }
    
    /* Style des boutons HTML personnalisés */
    .nav-button {
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 15px 5px;
        margin-bottom: 10px;
        border-radius: 12px;
        color: white !important;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        min-height: 65px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logique de chargement
DOSSIER_CHEMIN = "data"
FICHIER_URLS = os.path.join(DOSSIER_CHEMIN, "Url_Liste_Modifiable_2.txt")
FICHIER_LISTES = os.path.join(DOSSIER_CHEMIN, "Url_Liste_Modifiable.txt")

def charger_donnees(chemin_fichier):
    data = []
    if not os.path.exists(chemin_fichier): return data
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"): continue
                parts = [p.strip() for p in ligne.split(",")]
                if len(parts) >= 2:
                    data.append({
                        "nom": parts[0], 
                        "cible": parts[1], 
                        "couleur": parts[2] if len(parts) > 2 else "#8e44ad"
                    })
    except: pass
    return data

# 4. Interface
st.markdown("<h1>WEB NAVIGATION HUB</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🌐 URLS DIRECTES", "📁 LISTES TXT"])

def afficher_grille(fichier):
    items = charger_donnees(fichier)
    if not items:
        st.info("Aucune donnée.")
        return

    # On utilise les colonnes standards de Streamlit
    # Mais le CSS injecté plus haut les empêchera de s'empiler
    for i in range(0, len(items), 2):
        cols = st.columns(2)
        
        # Premier bouton de la ligne
        with cols[0]:
            item = items[i]
            nom = item['nom'].replace('\\n', '<br>')
            st.markdown(f'<a href="{item["cible"]}" target="_blank" class="nav-button" style="background-color: {item["couleur"]};">{nom}</a>', unsafe_allow_html=True)
        
        # Deuxième bouton (si il existe)
        if i + 1 < len(items):
            with cols[1]:
                item = items[i+1]
                nom = item['nom'].replace('\\n', '<br>')
                st.markdown(f'<a href="{item["cible"]}" target="_blank" class="nav-button" style="background-color: {item["couleur"]};">{nom}</a>', unsafe_allow_html=True)

with tab1:
    afficher_grille(FICHIER_URLS)

with tab2:
    afficher_grille(FICHIER_LISTES)

# Footer simple
st.write("---")
if st.button("🔄 ACTUALISER", use_container_width=True):
    st.rerun()
