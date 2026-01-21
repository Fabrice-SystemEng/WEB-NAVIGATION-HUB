from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
import webbrowser
import os

# Configuration du fond (Noir profond)
Window.clearcolor = (0.06, 0.07, 0.1, 1)

class ModernButton(Button):
    """Bouton personnalisé avec coins arrondis"""
    def __init__(self, rounded_color, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)  # On cache le fond standard
        self.rounded_color = rounded_color
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.rounded_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[15,])

class NexusHubApp(App):
    def build(self):
        self.title = "NEXUS HUB"
        self.repertoire_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # 1. Header stylisé
        header = Label(
            text="WEB NAVIGATION HUB", 
            font_size='22sp', bold=True, color=(0.32, 0.66, 1, 1),
            size_hint_y=None, height=50
        )
        main_layout.add_widget(header)

        # 2. Boutons de contrôle discrets
        control_bar = BoxLayout(size_hint_y=None, height=45, spacing=10)
        btn_refresh = ModernButton(text="ACTUALISER", rounded_color=(0.15, 0.18, 0.25, 1), size_hint_x=0.5)
        btn_refresh.bind(on_release=self.refresh_app)
        btn_folder = ModernButton(text="SOURCE", rounded_color=(0.15, 0.18, 0.25, 1), size_hint_x=0.5)
        btn_folder.bind(on_release=self.ouvrir_repertoire)
        
        control_bar.add_widget(btn_refresh)
        control_bar.add_widget(btn_folder)
        main_layout.add_widget(control_bar)

        # 3. Système d'onglets
        self.tp = TabbedPanel(do_default_tab=False, background_color=(0,0,0,0))
        self.tp.tab_width = Window.width / 2.2
        
        self.tab1 = TabbedPanelItem(text="LISTES TXT")
        self.tab1.add_widget(self.creer_grille("Url_Liste_Modifiable_2.txt"))
        
        self.tab2 = TabbedPanelItem(text="URLS DIRECTES")
        self.tab2.add_widget(self.creer_grille("Url_Liste_Modifiable.txt"))
        
        self.tp.add_widget(self.tab1)
        self.tp.add_widget(self.tab2)
        
        main_layout.add_widget(self.tp)
        return main_layout

    def creer_grille(self, nom_fichier):
        scroll = ScrollView(bar_width=0)
        # CHANGEMENT : cols=3 pour avoir 3 colonnes, spacing réduit à 8 pour gagner de la place
        grid = GridLayout(cols=3, spacing=8, size_hint_y=None, padding=[5, 15, 5, 15])
        grid.bind(minimum_height=grid.setter('height'))
        
        items = self.charger_donnees(nom_fichier)
        for item in items:
            btn = ModernButton(
                text=item["nom"].replace('\\n', '\n'),
                rounded_color=self.hex_to_rgb(item["couleur"]),
                font_size='12sp', bold=True, # Taille de police légèrement réduite (12sp au lieu de 14sp)
                size_hint_y=None, height=90 # Hauteur réduite (90 au lieu de 110)
            )
            btn.bind(on_release=lambda x, url=item["cible"]: webbrowser.open(url))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        return scroll

    def charger_donnees(self, nom_fichier):
        data = []
        chemin = os.path.join(self.repertoire_data, nom_fichier)
        if not os.path.exists(chemin): return data
        with open(chemin, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"): continue
                p = [i.strip() for i in ligne.split(",")]
                if len(p) >= 2:
                    data.append({"nom": p[0], "cible": p[1], "couleur": p[2] if len(p)>2 else "#8e44ad"})
        return data

    def refresh_app(self, instance):
        self.tab1.clear_widgets()
        self.tab1.add_widget(self.creer_grille("Url_Liste_Modifiable_2.txt"))
        self.tab2.clear_widgets()
        self.tab2.add_widget(self.creer_grille("Url_Liste_Modifiable.txt"))

    def ouvrir_repertoire(self, instance):
        webbrowser.open(f"https://github.com/Fabrice-SystemEng/WEB-NAVIGATION-HUB")

    def hex_to_rgb(self, hex_str):
        hex_str = hex_str.lstrip('#')
        return [int(hex_str[i:i+2], 16)/255.0 for i in (0, 2, 4)] + [1]

if __name__ == '__main__':
    NexusHubApp().run()
