import streamlit as st
import os

# ================================================================
# ===========  BLOC DE FORCE POUR LE NOM ET L'ICÔNE  =============
st.set_page_config(page_title="NEXUS HUB", page_icon="💠", layout="wide")

# Ce code HTML force le nom pour les mobiles Android/Samsung
st.markdown(f"""
    <head>
        <title>URL HUB</title>
        <meta name="apple-mobile-web-app-title" content="URL HUB">
        <meta name="application-name" content="URL HUB">
    </head>
    """, unsafe_allow_html=True)

# ================================================================
# ===================     Configuration     ======================

# config de base : st.set_page_config(page_title="WEB NAVIGATION HUB", layout="wide")
st.set_page_config(
    page_title="WEB NAVIGATION HUB", 
    page_icon="🚀",  # Exemples d'options possibles 🌐, 🛰️, 🧭 ou 📱
    layout="wide"
)

# Dossier de données
DOSSIER_CHEMIN = "data" 
if not os.path.exists(DOSSIER_CHEMIN):
    os.makedirs(DOSSIER_CHEMIN)

# Fichiers sources
FICHIER_URLS = os.path.join(DOSSIER_CHEMIN, "Url_Liste_Modifiable_2.txt")
FICHIER_LISTES = os.path.join(DOSSIER_CHEMIN, "Url_Liste_Modifiable.txt")

# URL de votre dépôt GitHub (CORRIGÉE ICI)
GITHUB_REPO_URL = "https://github.com/Fabrice-SystemEng/WEB-NAVIGATION-HUB"

# ================================================================
# =================    Fonctions Logique    ======================

def charger_donnees(chemin_fichier):
    data = []
    if not os.path.exists(chemin_fichier): return data
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"): continue
                parts = [p.strip() for p in ligne.split(",")]
                nom = parts[0]
                cible = parts[1] if len(parts) > 1 else ""
                couleur = parts[2] if len(parts) > 2 else "#8e44ad"
                data.append({"nom": nom, "cible": cible, "couleur": couleur})
    except Exception as e:
        st.error(f"Erreur de lecture : {e}")
    return data

# ================================================================
# =================      Interface Web       =====================

st.markdown(f"""
    <style>
    .main {{ background-color: #0F111A; }}
    h1 {{ text-align: center; color: #51A8FF; font-family: 'Segoe UI'; padding-bottom: 10px; }}
    
    .stTabs [data-baseweb="tab-list"] {{ gap: 8px; }}
    .stTabs [data-baseweb="tab"] {{
        background-color: #1A1D2E;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #9CA3AF;
    }}
    .stTabs [aria-selected="true"] {{ color: #51A8FF !important; border-bottom: 2px solid #51A8FF !important; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>WEB NAVIGATION HUB</h1>", unsafe_allow_html=True)

# Onglets (URLS DIRECTES par défaut)
tab1, tab2 = st.tabs(["🌐 URLS DIRECTES", "📁 LISTES TXT"])

def afficher_boutons(fichier):
    items = charger_donnees(fichier)
    if not items:
        st.info("Aucune donnée trouvée.")
        return

    cols = st.columns(3)
    for i, item in enumerate(items):
        with cols[i % 2]:
            if item["cible"]:
                st.markdown(f"""
                    <a href="{item['cible']}" target="_blank" style="text-decoration: none;">
                        <div style="
                            background-color: {item['couleur']};
                            padding: 20px;
                            margin: 8px 0;
                            border-radius: 15px;
                            text-align: center;
                            color: white;
                            font-weight: bold;
                            font-size: 16px;
                            min-height: 70px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
                        ">
                            {item['nom'].replace('\\n', '<br>')}
                        </div>
                    </a>
                """, unsafe_allow_html=True)
            else:
                st.button(item["nom"], disabled=True, key=f"dis_{i}_{fichier}")

with tab1:
    afficher_boutons(FICHIER_URLS)

with tab2:
    afficher_boutons(FICHIER_LISTES)

# --- FOOTER ---
st.write("---")
col_f1, col_f2 = st.columns(3)

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
            ">
                📂 OUVRIR RÉPERTOIRE SOURCE
            </div>
        </a>
    """, unsafe_allow_html=True)
