import streamlit as st
import os

# Version 2025-12
## MAJ 2026-01-21 : Modifier pour avoir 2 colonnes sur android (CSS Grid personnalisé au lieu de st.columns)

# ================================================================
# ===========  BLOC DE FORCE POUR LE NOM ET L'ICÔNE  =============
# Note : On ne garde qu'un seul set_page_config (le premier est celui qui compte)
st.set_page_config(
    page_title="NEXUS HUB", 
    page_icon="💠", 
    layout="wide"
)

# Ce code HTML force le nom pour les mobiles Android/Samsung
st.markdown("""
    <head>
        <title>URL HUB</title>
        <meta name="apple-mobile-web-app-title" content="URL HUB">
        <meta name="application-name" content="URL HUB">
    </head>
    """, unsafe_allow_html=True)

# ================================================================
# ===================      Configuration      ======================

DOSSIER_CHEMIN = "data" 
if not os.path.exists(DOSSIER_CHEMIN):
    os.makedirs(DOSSIER_CHEMIN)

FICHIER_URLS = os.path.join(DOSSIER_CHEMIN, "Url_Liste_Modifiable_2.txt")
FICHIER_LISTES = os.path.join(DOSSICH_CHEMIN, "Url_Liste_Modifiable.txt")
GITHUB_REPO_URL = "https://github.com/Fabrice-SystemEng/WEB-NAVIGATION-HUB"

# ================================================================
# =================  --- Fonctions Logique ---  ==================

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
    except Exception as e:
        st.error(f"Erreur de lecture : {e}")
    return data

# ================================================================
# =================      Interface Web        =====================

st.markdown("""
    <style>
    .main { background-color: #0F111A; }
    h1 { text-align: center; color: #51A8FF; font-family: 'Segoe UI'; padding-bottom: 10px; }
    
    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1A1D2E;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #9CA3AF;
    }
    .stTabs [aria-selected="true"] { color: #51A8FF !important; border-bottom: 2px solid #51A8FF !important; }

    /* LE CONTENEUR DE GRILLE FORCEE */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* FORCE 2 COLONNES */
        gap: 12px;
        padding: 10px 0;
    }

    .custom-button {
        text-decoration: none;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-weight: bold;
        font-size: 14px;
        min-height: 80px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        transition: transform 0.1s;
    }
    .custom-button:active { transform: scale(0.95); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>WEB NAVIGATION HUB</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🌐 URLS DIRECTES", "📁 LISTES TXT"])

def afficher_boutons(fichier):
    items = charger_donnees(fichier)
    if not items:
        st.info("Aucune donnée trouvée.")
        return

    # On crée une chaîne HTML pour toute la grille
    html_grid = '<div class="grid-container">'
    
    for item in items:
        nom_affiche = item['nom'].replace('\\n', '<br>')
        html_grid += f"""
            <a href="{item['cible']}" target="_blank" class="custom-button" style="background-color: {item['couleur']};">
                {nom_affiche}
            </a>
        """
    
    html_grid += '</div>'
    st.markdown(html_grid, unsafe_allow_html=True)

with tab1:
    afficher_boutons(FICHIER_URLS)

with tab2:
    afficher_boutons(FICHIER_LISTES)

# --- FOOTER ---
st.write("---")
# Ici on garde st.columns pour le footer car 2 gros boutons côte à côte sont mieux empilés sur petit mobile
col_f1, col_f2 = st.columns(2)

with col_f1:
    if st.button("🔄 ACTUALISER LES DONNÉES", use_container_width=True):
        st.rerun()

with col_f2:
    st.markdown(f"""
        <a href="{GITHUB_REPO_URL}" target="_blank" style="text-decoration: none;">
            <div style="
                background-color: transparent;
                border: 1px solid #333333;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                color: #9CA3AF;
                font-size: 14px;
                font-weight: bold;
                height: 45px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                📂 RÉPERTOIRE SOURCE
            </div>
        </a>
    """, unsafe_allow_html=True)
