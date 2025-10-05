# dashboard_defense_coree_nord.py
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
    page_title="Analyse de la Défense Nord-Coréenne - RPDC",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        background: linear-gradient(45deg, #024FA2, #ED1C27, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #024FA2;
        margin: 0.5rem 0;
    }
    .section-header {
        color: #ED1C27;
        border-bottom: 2px solid #024FA2;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .pays-card {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 5px solid #ED1C27;
        background-color: #f8f9fa;
    }
    .coreen-flag {
        background: linear-gradient(45deg, #024FA2, #ED1C27, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .juche-card {
        background: linear-gradient(135deg, #024FA2, #ED1C27);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseCoreeNordDashboard:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        
    def define_branches_options(self):
        """Définit les branches militaires disponibles pour l'analyse"""
        return [
            "Armée Populaire de Corée", "Forces Terrestres", "Forces Maritimes", 
            "Forces Aériennes", "Forces Stratégiques", "Forces Spéciales"
        ]
    
    def define_programmes_options(self):
        """Définit les programmes militaires disponibles"""
        return [
            "Programme Nucléaire", "Programme Missilistique", "Forces Conventionnelles",
            "Cyber Défense", "Renseignement"
        ]
    
    def generate_defense_data(self, selection):
        """Génère des données de défense simulées pour le dashboard"""
        # Période d'analyse : 2012-2027
        annees = list(range(2012, 2028))
        
        # Configuration de base selon la sélection
        config = self.get_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_budget(annees, config),
            'Personnel_Milliers': self.simulate_personnel(annees, config),
            'Exercices_Militaires': self.simulate_military_exercises(annees, config),
            'Readiness_Operative': self.simulate_readiness(annees),
            'Capacite_Dissuasion': self.simulate_deterrence_capacity(annees),
            'Temps_Mobilisation_Jours': self.simulate_mobilization_time(annees),
            'Tests_Missiles': self.simulate_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees)
        }
        
        # Ajouter des indicateurs spécifiques
        if 'nucleaire' in config.get('priorites', []):
            data['Tests_Nucleaires'] = self.simulate_nuclear_tests(annees)
        if 'missiles' in config.get('priorites', []):
            data['Portee_Missiles_Km'] = self.simulate_missile_range(annees)
        if 'cyber' in config.get('priorites', []):
            data['Capacite_Cyber'] = self.simulate_cyber_capacity(annees)
        
        return pd.DataFrame(data), config
    
    def get_config(self, selection):
        """Retourne la configuration pour une branche/programme donné"""
        configs = {
            "Armée Populaire de Corée": {
                "type": "armee_totale",
                "budget_base": 3.5,
                "personnel_base": 1200,  # en milliers
                "exercices_base": 80,
                "priorites": ["nucleaire", "missiles", "conventionnel"]
            },
            "Forces Terrestres": {
                "type": "branche",
                "personnel_base": 950,  # en milliers
                "exercices_base": 45,
                "priorites": ["artillerie", "blindes", "forces_speciales"]
            },
            "Forces Maritimes": {
                "type": "branche", 
                "personnel_base": 60,  # en milliers
                "exercices_base": 25,
                "priorites": ["sous-marins", "navires_legers", "defense_cotiere"]
            },
            "Forces Aériennes": {
                "type": "branche",
                "personnel_base": 110,  # en milliers
                "exercices_base": 30,
                "priorites": ["defense_aerienne", "chasseurs", "transports"]
            },
            "Forces Stratégiques": {
                "type": "branche_speciale",
                "personnel_base": 15,  # en milliers
                "exercices_base": 12,
                "priorites": ["nucleaire", "missiles", "dissuasion"]
            },
            "Programme Nucléaire": {
                "type": "programme_strategique",
                "budget_base": 0.8,
                "priorites": ["recherche", "developpement", "essais"]
            },
            "Programme Missilistique": {
                "type": "programme_strategique",
                "budget_base": 1.2,
                "priorites": ["portee", "precision", "charges_multiples"]
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 100,
            "exercices_base": 20,
            "priorites": ["defense_generique"]
        })
    
    def simulate_budget(self, annees, config):
        """Simule l'évolution du budget défense"""
        budget_base = config.get('budget_base', 2.0)
        return [budget_base * (1 + 0.04 * (annee - 2012)) for annee in annees]
    
    def simulate_personnel(self, annees, config):
        """Simule l'évolution des effectifs (en milliers)"""
        personnel_base = config.get('personnel_base', 100)
        return [personnel_base * (1 + 0.01 * (annee - 2012)) for annee in annees]
    
    def simulate_military_exercises(self, annees, config):
        """Simule les exercices militaires"""
        base = config.get('exercices_base', 30)
        return [base + 2 * (annee - 2012) for annee in annees]
    
    def simulate_readiness(self, annees):
        """Simule le niveau de préparation opérationnelle"""
        return [min(70 + 2 * (annee - 2012), 95) for annee in annees]
    
    def simulate_deterrence_capacity(self, annees):
        """Simule la capacité de dissuasion"""
        return [min(40 + 5 * (annee - 2012), 90) for annee in annees]
    
    def simulate_mobilization_time(self, annees):
        """Simule le temps de mobilisation"""
        return [max(48 - 1.5 * (annee - 2012), 24) for annee in annees]
    
    def simulate_missile_tests(self, annees):
        """Simule les tests de missiles"""
        tests = []
        for annee in annees:
            if annee < 2015:
                tests.append(3 + (annee - 2012))
            elif annee < 2020:
                tests.append(6 + 2 * (annee - 2014))
            else:
                tests.append(16 + 3 * (annee - 2019))
        return tests
    
    def simulate_tech_development(self, annees):
        """Simule le développement technologique"""
        return [min(35 + 6 * (annee - 2012), 85) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Simule la capacité d'artillerie"""
        return [min(75 + 1.5 * (annee - 2012), 95) for annee in annees]
    
    def simulate_nuclear_tests(self, annees):
        """Simule les tests nucléaires"""
        tests = [0] * len(annees)
        # Tests réels simulés + développement continu
        for i, annee in enumerate(annees):
            if annee == 2013:
                tests[i] = 1
            elif annee == 2016:
                tests[i] = 2
            elif annee == 2017:
                tests[i] = 1
            elif annee >= 2022:
                tests[i] = min(1 + (annee - 2022), 3)
        return tests
    
    def simulate_missile_range(self, annees):
        """Simule la portée des missiles (en km)"""
        return [min(1300 + 300 * (annee - 2012), 15000) for annee in annees]
    
    def simulate_cyber_capacity(self, annees):
        """Simule la capacité cyber"""
        return [min(50 + 4 * (annee - 2012), 85) for annee in annees]
    
    def display_header(self):
        """Affiche l'en-tête du dashboard"""
        st.markdown('<h1 class="main-header">⭐ Analyse des Capacités Militaires de la RPDC</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="coreen-flag">🇰🇵 DÉFENSE ET DISSUASION STRATÉGIQUE 🇰🇵</div>', 
                       unsafe_allow_html=True)
            st.markdown("**Analyse stratégique des capacités militaires nord-coréennes (2012-2027)**")
    
    def create_sidebar(self):
        """Crée la sidebar avec les contrôles"""
        st.sidebar.markdown("## 🎛️ CONTRÔLES D'ANALYSE")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Type d'analyse:",
            ["Branches Militaires", "Programmes Stratégiques", "Vue d'Ensemble RPDC"]
        )
        
        if type_analyse == "Branches Militaires":
            selection = st.sidebar.selectbox("Sélectionnez une branche:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Sélectionnez un programme:", self.programmes_options)
        else:
            selection = "Armée Populaire de Corée"
        
        # Options d'affichage
        st.sidebar.markdown("### 📊 Options de visualisation")
        show_projection = st.sidebar.checkbox("Afficher les projections 2023-2027", value=True)
        show_juche_analysis = st.sidebar.checkbox("Analyse doctrine Juche", value=True)
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_projection': show_projection,
            'show_juche_analysis': show_juche_analysis
        }
    
    def display_key_metrics(self, df, config):
        """Affiche les métriques clés"""
        st.markdown('<h3 class="section-header">📊 INDICATEURS STRATÉGIQUES CLÉS</h3>', 
                   unsafe_allow_html=True)
        
        # Calcul des métriques
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2012 = df[df['Annee'] == 2012].iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if 'Budget_Defense_Mds' in df.columns:
                croissance_budget = ((data_actuelle['Budget_Defense_Mds'] - data_2012['Budget_Defense_Mds']) / 
                                   data_2012['Budget_Defense_Mds']) * 100
                st.metric(
                    "Budget Défense 2027",
                    f"{data_actuelle['Budget_Defense_Mds']:.1f} Md$",
                    f"{croissance_budget:+.1f}% vs 2012"
                )
        
        with col2:
            if 'Personnel_Milliers' in df.columns:
                evolution_personnel = ((data_actuelle['Personnel_Milliers'] - data_2012['Personnel_Milliers']) / 
                                     data_2012['Personnel_Milliers']) * 100
                st.metric(
                    "Effectifs 2027",
                    f"{data_actuelle['Personnel_Milliers']:,.0f} K",
                    f"{evolution_personnel:+.1f}% vs 2012"
                )
        
        with col3:
            croissance_dissuasion = ((data_actuelle['Capacite_Dissuasion'] - data_2012['Capacite_Dissuasion']) / 
                                   data_2012['Capacite_Dissuasion']) * 100
            st.metric(
                "Capacité Dissuasion 2027",
                f"{data_actuelle['Capacite_Dissuasion']:.1f}%",
                f"{croissance_dissuasion:+.1f}% vs 2012"
            )
        
        with col4:
            reduction_temps = ((data_2012['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2012['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "Temps Mobilisation 2027",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}% vs 2012"
            )
    
    def create_budget_analysis(self, df, config):
        """Analyse des budgets et effectifs"""
        st.markdown('<h3 class="section-header">💰 ANALYSE BUDGÉTAIRE ET EFFECTIFS</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if 'Budget_Defense_Mds' in df.columns:
                fig = px.line(df, x='Annee', y='Budget_Defense_Mds',
                             title="Évolution du Budget de Défense (2012-2027)",
                             labels={'Budget_Defense_Mds': 'Budget (Md$)', 'Annee': 'Année'})
                fig.update_traces(line=dict(color='#024FA2', width=3))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'Personnel_Milliers' in df.columns:
                fig = px.line(df, x='Annee', y='Personnel_Milliers',
                             title="Évolution des Effectifs (2012-2027)",
                             labels={'Personnel_Milliers': 'Effectifs (Milliers)', 'Annee': 'Année'})
                fig.update_traces(line=dict(color='#ED1C27', width=3))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    def create_military_activities_analysis(self, df, config):
        """Analyse des activités militaires"""
        st.markdown('<h3 class="section-header">⚔️ ACTIVITÉS MILITAIRES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.line(df, x='Annee', y='Exercices_Militaires',
                         title="Exercices Militaires (2012-2027)",
                         labels={'Exercices_Militaires': "Nombre d'exercices", 'Annee': 'Année'})
            fig.update_traces(line=dict(color='#024FA2', width=3))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'Tests_Missiles' in df.columns:
                fig = px.line(df, x='Annee', y='Tests_Missiles',
                             title="Tests de Missiles (2012-2027)",
                             labels={'Tests_Missiles': 'Nombre de tests', 'Annee': 'Année'})
                fig.update_traces(line=dict(color='#ED1C27', width=3))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    def create_capabilities_analysis(self, df, config):
        """Analyse des capacités opérationnelles"""
        st.markdown('<h3 class="section-header">⚡ CAPACITÉS OPÉRATIONNELLES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Graphique combiné des capacités
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(x=df['Annee'], y=df['Readiness_Operative'],
                                    mode='lines', name='Préparation Opérationnelle',
                                    line=dict(color='#024FA2', width=3)))
            
            fig.add_trace(go.Scatter(x=df['Annee'], y=df['Capacite_Dissuasion'],
                                    mode='lines', name='Capacité de Dissuasion',
                                    line=dict(color='#ED1C27', width=3)))
            
            if 'Capacite_Artillerie' in df.columns:
                fig.add_trace(go.Scatter(x=df['Annee'], y=df['Capacite_Artillerie'],
                                        mode='lines', name='Capacité Artillerie',
                                        line=dict(color='#FFCC00', width=3)))
            
            fig.update_layout(title="Évolution des Capacités Opérationnelles (2012-2027)",
                             xaxis_title="Année",
                             yaxis_title="Niveau (%)",
                             height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Temps de mobilisation
            fig = px.line(df, x='Annee', y='Temps_Mobilisation_Jours',
                         title="Temps de Mobilisation (2012-2027)",
                         labels={'Temps_Mobilisation_Jours': 'Jours', 'Annee': 'Année'})
            fig.update_traces(line=dict(color='#FF6600', width=3))
            fig.update_layout(height=500)
            fig.update_yaxes(autorange="reversed")  # Moins de jours = mieux
            st.plotly_chart(fig, use_container_width=True)
    
    def create_strategic_programs_analysis(self, df, config):
        """Analyse des programmes stratégiques"""
        st.markdown('<h3 class="section-header">🚀 PROGRAMMES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Tests nucléaires
            if 'Tests_Nucleaires' in df.columns:
                fig = px.bar(df, x='Annee', y='Tests_Nucleaires',
                            title="Tests Nucléaires (2012-2027)",
                            labels={'Tests_Nucleaires': 'Nombre de tests', 'Annee': 'Année'})
                fig.update_traces(marker_color='#ED1C27')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Portée des missiles
            if 'Portee_Missiles_Km' in df.columns:
                fig = px.line(df, x='Annee', y='Portee_Missiles_Km',
                             title="Portée Maximale des Missiles (2012-2027)",
                             labels={'Portee_Missiles_Km': 'Portée (km)', 'Annee': 'Année'})
                fig.update_traces(line=dict(color='#024FA2', width=3))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    def create_juche_analysis(self, df, config):
        """Analyse de la doctrine Juche"""
        st.markdown('<h3 class="section-header">🎯 DOCTRINE JUCHE ET AUTOSUFFISANCE</h3>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div class="juche-card">
        <h4>🎯 Principes de la Doctrine Juche</h4>
        <ul>
        <li><strong>Autosuffisance militaire</strong> - Développement autonome des capacités</li>
        <li><strong>Indépendance politique</strong> - Prise de décision souveraine</li>
        <li><strong>Autodéfense nationale</strong> - Capacité à défendre le territoire</li>
        <li><strong>Priorité aux forces armées</strong> - L'armée comme pilier de la société</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Développement technologique
            fig = px.line(df, x='Annee', y='Developpement_Technologique',
                         title="Développement Technologique Autonome (2012-2027)",
                         labels={'Developpement_Technologique': 'Niveau (%)', 'Annee': 'Année'})
            fig.update_traces(line=dict(color='#024FA2', width=3))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Indice d'autosuffisance
            autosuffisance = [min(60 + 3 * (annee - 2012), 85) for annee in df['Annee']]
            fig = px.line(x=df['Annee'], y=autosuffisance,
                         title="Niveau d'Autosuffisance Militaire (2012-2027)",
                         labels={'x': 'Année', 'y': 'Autosuffisance (%)'})
            fig.update_traces(line=dict(color='#ED1C27', width=3))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_comparative_analysis(self, df, config):
        """Analyse comparative avant/après développement stratégique"""
        st.markdown('<h3 class="section-header">📊 ANALYSE COMPARATIVE</h3>', 
                   unsafe_allow_html=True)
        
        # Calcul des moyennes avant et après 2017 (accélération des programmes)
        avant_2017 = df[df['Annee'] <= 2017]
        apres_2017 = df[df['Annee'] > 2017]
        
        if len(avant_2017) > 0 and len(apres_2017) > 0:
            indicateurs = ['Capacite_Dissuasion', 'Tests_Missiles', 'Developpement_Technologique']
            noms = ['Capacité Dissuasion', 'Tests Missiles', 'Développement Techno']
            
            valeurs_avant = [avant_2017[ind].mean() for ind in indicateurs]
            valeurs_apres = [apres_2017[ind].mean() for ind in indicateurs]
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(name='2012-2017', x=noms, y=valeurs_avant,
                                marker_color='#024FA2'))
            fig.add_trace(go.Bar(name='2018-2027', x=noms, y=valeurs_apres,
                                marker_color='#ED1C27'))
            
            fig.update_layout(title="Comparaison Avant/Après Accélération Stratégique",
                             barmode='group',
                             height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_strategic_insights(self, df, config, selection):
        """Génère des insights stratégiques"""
        st.markdown('<h3 class="section-header">💡 ANALYSE STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        # Calcul des indicateurs de performance
        croissance_dissuasion = ((df['Capacite_Dissuasion'].iloc[-1] - df['Capacite_Dissuasion'].iloc[0]) / 
                               df['Capacite_Dissuasion'].iloc[0]) * 100
        
        reduction_temps = ((df['Temps_Mobilisation_Jours'].iloc[0] - df['Temps_Mobilisation_Jours'].iloc[-1]) / 
                         df['Temps_Mobilisation_Jours'].iloc[0]) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 PROGRÈS STRATÉGIQUES")
            st.markdown(f"""
            - **Capacité de dissuasion**: +{croissance_dissuasion:.1f}% depuis 2012
            - **Temps de mobilisation**: -{reduction_temps:.1f}% depuis 2012  
            - **Exercices militaires**: {df['Exercices_Militaires'].iloc[-1]:.0f} par an
            - **Préparation opérationnelle**: {df['Readiness_Operative'].iloc[-1]:.0f}%
            """)
            
            if 'Tests_Missiles' in df.columns:
                tests_totaux = df['Tests_Missiles'].sum()
                st.markdown(f"- **Tests missiles totaux**: {tests_totaux:.0f}")
        
        with col2:
            st.markdown("#### 🚀 AXES STRATÉGIQUES")
            
            if config['type'] in ['armee_totale', 'branche']:
                st.markdown("""
                - Renforcement capacités de dissuasion
                - Modernisation équipements conventionnels
                - Développement forces asymétriques
                - Amélioration préparation opérationnelle
                """)
            elif config['type'] == 'programme_strategique':
                st.markdown("""
                - Accélération développement technologique
                - Augmentation portée et précision
                - Diversification capacités
                - Renforcement effets stratégiques
                """)
        
        # Analyse des priorités
        if config['type'] in ['armee_totale', 'branche', 'programme_strategique']:
            st.markdown("#### 🌟 PRIORITÉS STRATÉGIQUES")
            priorites = config.get('priorites', [])
            if priorites:
                for priorite in priorites:
                    st.markdown(f"- {priorite.replace('_', ' ').title()}")
    
    def create_korean_overview(self):
        """Vue d'ensemble nord-coréenne"""
        st.markdown('<h3 class="section-header">🌍 VUE D\'ENSEMBLE DES CAPACITÉS</h3>', 
                   unsafe_allow_html=True)
        
        # Données comparatives des différentes branches
        branches_principales = ["Forces Terrestres", "Forces Maritimes", "Forces Aériennes", "Forces Stratégiques"]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 👥 EFFECTIFS PAR BRANCHE (2027)")
            effectifs = {
                "Forces Terrestres": 950,
                "Forces Maritimes": 60, 
                "Forces Aériennes": 110,
                "Forces Stratégiques": 15
            }
            for branche, eff in effectifs.items():
                st.progress(eff/max(effectifs.values()), text=f"{branche}: {eff}K")
        
        with col2:
            st.markdown("#### ⚔️ CAPACITÉS PRINCIPALES")
            capacites = {
                "Artillerie": 95,
                "Missiles Court-Moyenne Portée": 85,
                "Missiles Longue Portée": 65,
                "Forces Spéciales": 90
            }
            for capacite, niveau in capacites.items():
                st.progress(niveau/100, text=f"{capacite}: {niveau}%")
        
        with col3:
            st.markdown("#### 🚀 PROGRAMMES STRATÉGIQUES")
            programmes = {
                "Missiles Balistiques": 8,
                "Technologie Nucléaire": 7,
                "Cyber Défense": 6,
                "Systèmes de Guidage": 7
            }
            for programme, niveau in programmes.items():
                st.progress(niveau/10, text=f"{programme}: {niveau}/10")

    def run_dashboard(self):
        """Exécute le dashboard complet"""
        # Sidebar
        controls = self.create_sidebar()
        
        # Header
        self.display_header()
        
        # Génération des données
        df, config = self.generate_defense_data(controls['selection'])
        
        # Navigation par onglets
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 Vue d'Ensemble", 
            "💰 Budgets & Effectifs", 
            "⚔️ Activités Militaires", 
            "⚡ Capacités", 
            "🚀 Programmes Stratégiques",
            "🌍 Analyse RPDC"
        ])
        
        with tab1:
            st.markdown(f"## ⭐ Analyse Militaire - {controls['selection']}")
            self.display_key_metrics(df, config)
            self.create_strategic_insights(df, config, controls['selection'])
        
        with tab2:
            self.create_budget_analysis(df, config)
        
        with tab3:
            self.create_military_activities_analysis(df, config)
        
        with tab4:
            self.create_capabilities_analysis(df, config)
        
        with tab5:
            self.create_strategic_programs_analysis(df, config)
            if controls['show_juche_analysis']:
                self.create_juche_analysis(df, config)
        
        with tab6:
            self.create_korean_overview()
            
            st.markdown("---")
            st.markdown("""
            #### 📋 À PROPOS DE CE DASHBOARD
            
            Ce dashboard présente une analyse stratégique des capacités militaires 
            de la République Populaire Démocratique de Corée (RPDC) depuis 2012.
            
            **Période d'analyse**: 2012-2027  
            **Indicateurs suivis**: 
            - Budgets de défense et effectifs
            - Exercices et tests militaires
            - Capacités de dissuasion stratégique
            - Développement technologique
            - Programmes stratégiques
            
            **Doctrine militaire**: Basée sur les principes Juche d'autosuffisance 
            et de défense nationale indépendante.
            
            *Note: Ce dashboard utilise des données estimées et simulées pour l'analyse stratégique.*
            """)

# Lancement du dashboard
if __name__ == "__main__":
    dashboard = DefenseCoreeNordDashboard()
    dashboard.run_dashboard()