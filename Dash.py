# dashboard_defense_coree_nord_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - RPDC",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #024FA2, #ED1C27, #FFFFFF, #FFCC00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #ED1C27;
        border-bottom: 3px solid #024FA2;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .juche-card {
        background: linear-gradient(135deg, #024FA2, #ED1C27);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .warning-card {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .success-card {
        background: linear-gradient(135deg, #00b894, #55a630);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .nuclear-card {
        background: linear-gradient(135deg, #e17055, #d63031);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseCoreeNordDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.missile_types = self.define_missile_types()
        self.nuclear_facilities = self.define_nuclear_facilities()
        
    def define_branches_options(self):
        return [
            "Armée Populaire de Corée", "Forces Terrestres", "Forces Maritimes", 
            "Forces Aériennes", "Forces de Missiles Stratégiques", "Forces Spéciales",
            "Forces Cyber", "Garde Rouge"
        ]
    
    def define_programmes_options(self):
        return [
            "Programme Nucléaire Militaire", "Programme Missilistique", "Défense Anti-Missile",
            "Guerre Électronique", "Reconnaissance Spatiale", "Drones de Combat"
        ]
    
    def define_missile_types(self):
        return {
            "Missiles Balistiques à Courte Portée": {"portee": 1000, "precision": 50, "deploiement": 2010},
            "Missiles Balistiques à Moyenne Portée": {"portee": 3000, "precision": 100, "deploiement": 2016},
            "Missiles Balistiques Intercontinentaux": {"portee": 15000, "precision": 500, "deploiement": 2017},
            "Missiles de Croisière": {"portee": 2000, "precision": 10, "deploiement": 2020},
            "Missiles Sol-Air": {"portee": 400, "precision": 5, "deploiement": 2015}
        }
    
    def define_nuclear_facilities(self):
        return {
            "Yongbyon": {"type": "Complexe Nucléaire", "status": "Actif", "capacite": "Plutonium"},
            "Punggye-ri": {"type": "Site d'Essais", "status": "Actif", "capacite": "Essais Souterrains"},
            "Kangson": {"type": "Enrichissement Uranium", "status": "Actif", "capacite": "Uranium HEU"},
            "Sinpo": {"type": "Sous-marins Nucléaires", "status": "Développement", "capacite": "SLBM"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Tests_Missiles': self.simulate_detailed_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Munitions': self.simulate_ammunition_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal(annees),
                'Portee_Max_Missiles_Km': self.simulate_missile_range_evolution(annees),
                'Tetes_Multiples': self.simulate_mirv_development(annees),
                'Essais_Souterrains': self.simulate_underground_tests(annees)
            })
        
        if 'missiles' in config.get('priorites', []):
            data.update({
                'Precision_Missiles_Metres': self.simulate_missile_accuracy(annees),
                'Taux_Success_Lancement': self.simulate_launch_success_rate(annees),
                'Diversification_Plateformes': self.simulate_platform_diversification(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails"""
        configs = {
            "Armée Populaire de Corée": {
                "type": "armee_totale",
                "budget_base": 2.5,
                "personnel_base": 1100,
                "exercices_base": 70,
                "priorites": ["nucleaire", "missiles", "conventionnel", "cyber", "asymetrique"],
                "doctrines": ["Juche", "Songun", "Dissuasion Asymétrique"],
                "capacites_speciales": ["Guerre de Guérilla", "Artillerie Massive", "Forces Spéciales"]
            },
            "Forces de Missiles Stratégiques": {
                "type": "branche_strategique",
                "personnel_base": 25,
                "exercices_base": 15,
                "priorites": ["icbm", "irbm", "mrv", "penetration"],
                "missiles_deployes": ["Hwasong-15", "Hwasong-17", "Pukguksong-3"],
                "zones_cibles": ["Continental US", "Guam", "Japon", "Corée du Sud"]
            },
            "Forces Cyber": {
                "type": "branche_moderne",
                "personnel_base": 8,
                "exercices_base": 25,
                "priorites": ["cyber_espionnage", "cyber_attaque", "cyber_defense"],
                "unites_speciales": ["Bureau 121", "Groupes Lazarus", "Unités Reconnaissance"],
                "capacites_connues": ["DDoS", "Malware Avancé", "Phishing Ciblé"]
            },
            "Programme Nucléaire Militaire": {
                "type": "programme_strategique",
                "budget_base": 0.6,
                "priorites": ["ogives_tactiques", "ogives_strategiques", "miniaturisation"],
                "materiaux": ["Plutonium-239", "Uranium Hautement Enrichi"],
                "estimations_stock": "40-50 ogives nucléaires"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 100,
            "exercices_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 2.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.035 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2006 <= annee <= 2009:  # Période de tensions
                base *= 1.1
            elif 2013 <= annee <= 2017:  # Accélération programme nucléaire
                base *= 1.15
            elif annee >= 2022:  # Modernisation avancée
                base *= 1.2
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 100)
        return [personnel_base * (1 + 0.008 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [22 + 0.2 * (annee - 2000) for annee in annees]  # Estimation élevée
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 30)
        return [base + 3 * (annee - 2000) + 5 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 65 + 1.5 * (annee - 2000)
            if annee >= 2010:
                base += 5  # Amélioration après modernisation
            if annee >= 2020:
                base += 8  # Nouvelles doctrines
            readiness.append(min(base, 95))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            if annee < 2006:
                base = 30  # Conventionnel uniquement
            elif annee < 2013:
                base = 45  # Début nucléaire
            elif annee < 2017:
                base = 65  # ICBM testés
            else:
                base = 80 + 2 * (annee - 2017)  # Capacité mature
            deterrence.append(min(base, 95))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(72 - 2 * (annee - 2000), 12) for annee in annees]
    
    def simulate_detailed_missile_tests(self, annees):
        """Tests de missiles détaillés"""
        tests = []
        for annee in annees:
            if annee < 2006:
                tests.append(1)
            elif annee < 2012:
                tests.append(2 + (annee - 2006))
            elif annee < 2017:
                tests.append(8 + 2 * (annee - 2012))
            else:
                tests.append(20 + 4 * (annee - 2017))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(30 + 3 * (annee - 2000), 85) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(70 + 2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(40 + 3 * (annee - 2000), 85) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(50 + 2.5 * (annee - 2000), 90) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(30 + 4 * (annee - 2000), 88) for annee in annees]
    
    def simulate_ammunition_production(self, annees):
        """Production de munitions (indice)"""
        return [min(60 + 2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_nuclear_arsenal(self, annees):
        """Évolution du stock d'ogives nucléaires"""
        stock = []
        for annee in annees:
            if annee < 2006:
                stock.append(0)
            elif annee < 2013:
                stock.append(max(5 + (annee - 2006), 10))
            elif annee < 2017:
                stock.append(15 + 3 * (annee - 2013))
            else:
                stock.append(30 + 4 * (annee - 2017))
        return stock
    
    def simulate_missile_range_evolution(self, annees):
        """Évolution de la portée maximale des missiles"""
        portee = []
        for annee in annees:
            if annee < 2006:
                portee.append(500)
            elif annee < 2012:
                portee.append(1000 + 200 * (annee - 2006))
            elif annee < 2017:
                portee.append(3000 + 1000 * (annee - 2012))
            else:
                portee.append(15000)  # ICBM opérationnels
        return portee
    
    def simulate_mirv_development(self, annees):
        """Développement des têtes multiples"""
        return [max(0, min(0 + 3 * (annee - 2017), 8)) for annee in annees]
    
    def simulate_underground_tests(self, annees):
        """Essais souterrains et préparation"""
        return [min(20 + 2 * (annee - 2000), 80) for annee in annees]
    
    def simulate_missile_accuracy(self, annees):
        """Amélioration de la précision des missiles"""
        return [max(2000 - 80 * (annee - 2000), 50) for annee in annees]
    
    def simulate_launch_success_rate(self, annees):
        """Taux de succès des lancements"""
        return [min(40 + 3 * (annee - 2000), 92) for annee in annees]
    
    def simulate_platform_diversification(self, annees):
        """Diversification des plateformes de lancement"""
        return [min(20 + 4 * (annee - 2000), 85) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [max(5 + 2 * (annee - 2010), 0) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(25 + 5 * (annee - 2010), 90) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(35 + 4 * (annee - 2010), 85) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🛡️ ANALYSE STRATÉGIQUE AVANCÉE - RPDC</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #024FA2, #ED1C27); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🇰🇵 SYSTÈME DE DÉFENSE INTÉGRÉ DE LA RÉPUBLIQUE POPULAIRE DÉMOCRATIQUE DE CORÉE</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Armée Populaire de Corée"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Escalation Modérée", "Modernisation Accélérée", "Crise Majeure"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="nuclear-card">
                <h4>☢️ CAPACITÉ NUCLÉAIRE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 Stock: {} ogives</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="cyber-card">
                <h4>💻 CAPACITÉS CYBER</h4>
                <h2>{:.0f}%</h2>
                <p>🔓 {} attaques/an</p>
            </div>
            """.format(data_actuelle['Cyber_Capabilities'], 
                     int(data_actuelle.get('Attaques_Cyber_Reussies', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_AD'] - data_2000['Couverture_AD']) / 
                           data_2000['Couverture_AD']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_AD']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Portee_Max_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Max_Missiles_Km'] - data_2000.get('Portee_Max_Missiles_Km', 500)) / 
                                   data_2000.get('Portee_Max_Missiles_Km', 500)) * 100
                st.metric(
                    "🎯 Portée Missiles Max",
                    f"{data_actuelle['Portee_Max_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_AD']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Défense Anti-Aérienne']
            couleurs = ['#024FA2', '#ED1C27', '#2d3436', '#00b894']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Stock_Ogives_Nucleaires' in df.columns:
                strategic_data.append(df['Stock_Ogives_Nucleaires'])
                strategic_names.append('Stock Ogives Nucléaires')
            
            if 'Tests_Missiles' in df.columns:
                strategic_data.append(df['Tests_Missiles'])
                strategic_names.append('Tests de Missiles')
            
            if 'Portee_Max_Missiles_Km' in df.columns:
                strategic_data.append(df['Portee_Max_Missiles_Km'] / 100)  # Normalisation
                strategic_names.append('Portée Missiles (km/100)')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des capacités de frappe
            st.markdown("""
            <div class="juche-card">
                <h4>🎯 ZONES DE COUVERTURE STRATÉGIQUE</h4>
                <p><strong>Missiles Courte Portée (≤1,000 km):</strong> Corée du Sud, Japon</p>
                <p><strong>Missiles Moyenne Portée (≤3,000 km):</strong> Guam, Bases US Pacifique</p>
                <p><strong>Missiles Intercontinentaux (≥15,000 km):</strong> Continental US</p>
                <p><strong>Forces Conventionnelles:</strong> Péninsule Coréenne</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="warning-card">
                <h4>⚠️ RELATIONS INTERNATIONALES</h4>
                <p><strong>Chine:</strong> Relations complexes - soutien limité</p>
                <p><strong>Russie:</strong> Coopération militaire croissante</p>
                <p><strong>USA/Corée du Sud:</strong> Hostilité déclarée</p>
                <p><strong>ONU:</strong> Sanctions multiples en place</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des sanctions
            sanctions_data = {
                'Année': [2006, 2009, 2013, 2016, 2017, 2022],
                'Sanctions': ['Résolution 1718', 'Résolution 1874', 'Résolution 2094', 
                            'Résolution 2270', 'Résolution 2371', 'Nouvelles sanctions'],
                'Impact': [3, 5, 6, 7, 8, 8]  # sur 10
            }
            sanctions_df = pd.DataFrame(sanctions_data)
            
            fig = px.bar(sanctions_df, x='Année', y='Impact', 
                        title="📉 IMPACT DES SANCTIONS INTERNATIONALES",
                        labels={'Impact': 'Niveau d\'Impact'},
                        color='Impact',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice d'autosuffisance
            autosuffisance = [min(55 + 2 * (annee - 2000), 85) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=autosuffisance,
                         title="🛠️ AUTOSUFFISANCE MILITAIRE - INDICE JUCHE",
                         labels={'x': 'Année', 'y': 'Niveau d\'Autosuffisance (%)'})
            fig.update_traces(fillcolor='rgba(237, 28, 39, 0.3)', line_color='#ED1C27')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['Artillerie K9', 'MLRS 240mm', 'Missiles KN-23', 'ICBM Hwasong-17', 
                           'Sous-marins Classe Sinpo', 'Drones de Reconnaissance'],
                'Portée (km)': [40, 60, 450, 15000, 2000, 500],
                'Précision (m)': [50, 100, 50, 500, 1000, 10],
                'Statut': ['Déployé', 'Déployé', 'Déployé', 'Testé', 'Développement', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Précision (m)', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Conventionnelles', 'Missiles Stratégiques', 
                          'Défense Anti-Aérienne', 'Capacités Cyber', 'Forces Spéciales'],
                'Niveau 2000': [40, 20, 30, 10, 60],
                'Niveau 2027': [75, 85, 70, 80, 90]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#024FA2'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#ED1C27'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="nuclear-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Yongbyon:</strong> Complexe nucléaire principal</p>
                <p><strong>Punggye-ri:</strong> Site d'essais nucléaires</p>
                <p><strong>Sanum-dong:</strong> Développement missiles</p>
                <p><strong>Sinpo:</strong> Base sous-marine</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE JUCHE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="juche-card">
                <h4>🎯 PRINCIPE JUCHE</h4>
                <p><strong>Autosuffisance:</strong> Développement autonome</p>
                <p><strong>Indépendance:</strong> Souveraineté absolue</p>
                <p><strong>Conscience:</strong> Rôle des masses</p>
                <p><strong>Créativité:</strong> Adaptation continue</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="juche-card">
                <h4>⚔️ DOCTRINE SONGUN</h4>
                <p><strong>Primauté militaire:</strong> Armée d'abord</p>
                <p><strong>Préparation permanente:</strong> État d'alerte</p>
                <p><strong>Dissuasion asymétrique:</strong> Faible vs Fort</p>
                <p><strong>Riposte massive:</strong> Réponse écrasante</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="juche-card">
                <h4>🛡️ STRATÉGIE DÉFENSIVE</h4>
                <p><strong>Défense proactive:</strong> Prévention active</p>
                <p><strong>Guerre de guérilla:</strong> Mobilisation populaire</p>
                <p><strong>Forces spéciales:</strong> Opérations derrière lignes</p>
                <p><strong>Artillerie massive:</strong> Frappe préemptive</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="success-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DE L'ARMÉE POPULAIRE</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Unité de commandement:</strong> Centralisation des décisions</div>
                <div><strong>• Mobilité et surprise:</strong> Opérations rapides et imprévisibles</div>
                <div><strong>• Utilisation du terrain:</strong> Avantage défensif naturel</div>
                <div><strong>• Guerre prolongée:</strong> Usure de l'adversaire</div>
                <div><strong>• Coordination politico-militaire:</strong> Direction unique</div>
                <div><strong>• Préparation logistique:</strong> Autosuffisance en munitions</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Invasion Terrestre', 'Frappe Aérienne', 'Blocus Naval', 
                                 'Cyber Attaque', 'Guerre Électronique', 'Opérations Spéciales'],
                'Probabilité': [0.3, 0.7, 0.5, 0.8, 0.6, 0.4],
                'Impact': [0.9, 0.7, 0.8, 0.5, 0.6, 0.4],
                'Niveau Préparation': [0.9, 0.8, 0.6, 0.7, 0.5, 0.8]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Attaque Limitée', 'Conflit Conventionnel', 'Escalade Nucléaire', 
                           'Guerre Prolongée', 'Intervention Internationale'],
                'Dissuasion': [0.8, 0.6, 0.9, 0.5, 0.7],
                'Défense': [0.7, 0.5, 0.3, 0.6, 0.4],
                'Riposte': [0.9, 0.8, 1.0, 0.7, 0.6]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Dissuasion', x=response_df['Scénario'], y=response_df['Dissuasion']),
                go.Bar(name='Défense', x=response_df['Scénario'], y=response_df['Défense']),
                go.Bar(name='Riposte', x=response_df['Scénario'], y=response_df['Riposte'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="warning-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement nucléaire:</strong> Diversification des vecteurs</div>
                <div><strong>• Modernisation conventionnelle:</strong> Artillerie et blindés</div>
                <div><strong>• Défense anti-aérienne:</strong> Couverture intégrée</div>
                <div><strong>• Capacités cyber:</strong> Guerre informationnelle</div>
                <div><strong>• Forces spéciales:</strong> Opérations asymétriques</div>
                <div><strong>• Résilience logistique:</strong> Autosuffisance accrue</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_missile_database(self):
        """Base de données des systèmes missiliers"""
        st.markdown('<h3 class="section-header">🚀 BASE DE DONNÉES DES SYSTÈMES MISSILIERS</h3>', 
                   unsafe_allow_html=True)
        
        missile_data = []
        for nom, specs in self.missile_types.items():
            missile_data.append({
                'Système': nom,
                'Portée (km)': specs['portee'],
                'Précision CEP (m)': specs['precision'],
                'Année Déploiement': specs['deploiement'],
                'Statut': 'Opérationnel' if specs['deploiement'] < 2020 else 'Développement',
                'Type Ogive': 'Conventionnelle/Nucléaire' if specs['portee'] > 1000 else 'Conventionnelle'
            })
        
        missiles_df = pd.DataFrame(missile_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(missiles_df, x='Portée (km)', y='Précision CEP (m)',
                           size='Portée (km)', color='Type Ogive',
                           hover_name='Système', log_x=True, log_y=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES MISSILIERS",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="nuclear-card">
                <h4>📋 INVENTAIRE MISSILISTIQUE</h4>
            """, unsafe_allow_html=True)
            
            for missile in missile_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{missile['Système']}</strong><br>
                    📏 {missile['Portée (km)']:,} km • 🎯 {missile['Précision CEP (m)']} m<br>
                    📅 {missile['Année Déploiement']} • {missile['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "🚀 Systèmes d'Armes",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_missile_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - RPDC</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="juche-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="success-card" style="margin: 0.5rem 0;">
                        <strong>☢️ Capacité Nucléaire Opérationnelle</strong>
                        <p>Forces de dissuasion crédibles avec capacités de seconde frappe</p>
                    </div>
                    <div class="success-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Arsenal Missilistique Diversifié</strong>
                        <p>Couverture complète des cibles régionales et continentales</p>
                    </div>
                    <div class="success-card" style="margin: 0.5rem 0;">
                        <strong>⚔️ Forces Conventionnelles Massives</strong>
                        <p>Supériorité numérique et préparation opérationnelle élevée</p>
                    </div>
                    <div class="success-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Défense Territoriale Intégrée</strong>
                        <p>Réseaux défensifs profonds et préparation de la mobilisation</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="warning-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="warning-card" style="margin: 0.5rem 0;">
                        <strong>💸 Contraintes Économiques</strong>
                        <p>Sanctions internationales limitant l'accès aux technologies</p>
                    </div>
                    <div class="warning-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Obsolescence Technologique</strong>
                        <p>Équipements vieillissants dans certains domaines conventionnels</p>
                    </div>
                    <div class="warning-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Isolement Diplomatique</strong>
                        <p>Coopération militaire limitée avec partenaires étrangers</p>
                    </div>
                    <div class="warning-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Dépendance Énergétique</strong>
                        <p>Vulnérabilités logistiques en cas de conflit prolongé</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DOMAINE MISSILISTIQUE</h5>
                    <p>• SLBM opérationnels<br>• Têtes multiples (MIRV)<br>• Hypersonique<br>• Satellites militaires</p>
                </div>
                <div>
                    <h5>☢️ CAPACITÉS NUCLÉAIRES</h5>
                    <p>• Ogives tactiques<br>• Essais souterrains<br>• Second strike<br>• Miniaturisation</p>
                </div>
                <div>
                    <h5>💻 DOMAINE CYBER</h5>
                    <p>• Cyber commandement<br>• Guerre électronique<br>• Espionnage avancé<br>• Drones de combat</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="juche-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Modernisation continue des forces conventionnelles<br>
                    • Renforcement de la défense anti-aérienne<br>
                    • Développement des capacités anti-navires<br>
                    • Préparation de la mobilisation générale</p>
                </div>
                <div>
                    <h5>⚡ DISSUASION AVANCÉE</h5>
                    <p>• Diversification des vecteurs nucléaires<br>
                    • Sécurisation de la seconde frappe<br>
                    • Développement capacités asymétriques<br>
                    • Renforcement guerre électronique</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseCoreeNordDashboardAvance()
    dashboard.run_advanced_dashboard()