import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("""# 🚢 Analyse Exploratoire (EDA) - Généralisation
Ce notebook contient l'exploration initiale des données de la phase de **Généralisation** (Sujet 3).
Nous allons analyser les 4 fichiers principaux :
- `ships_large.csv`
- `radio_signatures_large.csv`
- `ais_data_large.csv`
- `anomalies_large.csv`
"""))

# Imports
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="whitegrid")

# Définition des chemins
DATA_DIR = '../SujetsHackathon2026/Sujet3/Généralisation'

# Chargement des données
ships_df = pd.read_csv(f'{DATA_DIR}/ships_large.csv')
radio_df = pd.read_csv(f'{DATA_DIR}/radio_signatures_large.csv')
ais_df = pd.read_csv(f'{DATA_DIR}/ais_data_large.csv')
anomalies_df = pd.read_csv(f'{DATA_DIR}/anomalies_large.csv')

print("Toutes les données ont été chargées avec succès !")
"""))

# Ships EDA
cells.append(nbf.v4.new_markdown_cell("""## 1. Analyse des Navires (`ships_large.csv`)
Cette section nous permet de comprendre le registre officiel des navires : leur pavillon (flag), leur type, et leurs caractéristiques physiques.
"""))

cells.append(nbf.v4.new_code_cell("""# Aperçu et informations générales
display(ships_df.info())
display(ships_df.head())
"""))

cells.append(nbf.v4.new_code_cell("""# Statistiques descriptives sur les valeurs numériques (longueur, largeur, année de construction, etc.)
display(ships_df.describe())
"""))

cells.append(nbf.v4.new_code_cell("""# Visualisation : Top 10 des pavillons (Flags)
plt.figure(figsize=(10, 5))
sns.countplot(data=ships_df, y='flag', order=ships_df['flag'].value_counts().iloc[:10].index, palette='Blues_r')
plt.title('Top 10 des Pavillons (Flags)')
plt.xlabel('Nombre de navires')
plt.ylabel('Pavillon')
plt.show()
"""))

# Radio Signatures EDA
cells.append(nbf.v4.new_markdown_cell("""## 2. Analyse des Signatures Radio (`radio_signatures_large.csv`)
Ce fichier contient les interceptions de signaux radio. Nous allons analyser la fréquence, la puissance, et les motifs d'impulsion (`pulse_pattern`).
"""))

cells.append(nbf.v4.new_code_cell("""display(radio_df.info())
display(radio_df.head())
"""))

cells.append(nbf.v4.new_code_cell("""# Distribution des fréquences
plt.figure(figsize=(10, 5))
sns.histplot(data=radio_df, x='frequency', bins=50, kde=True, color='purple')
plt.title('Distribution des Fréquences Radio (MHz)')
plt.xlabel('Fréquence')
plt.ylabel('Nombre d\\'interceptions')
plt.show()
"""))

cells.append(nbf.v4.new_code_cell("""# Répartition des motifs d'impulsion (Pulse Patterns)
plt.figure(figsize=(8, 5))
sns.countplot(data=radio_df, x='pulse_pattern', palette='magma')
plt.title('Distribution des Pulse Patterns')
plt.show()
"""))

# AIS EDA
cells.append(nbf.v4.new_markdown_cell("""## 3. Analyse des données AIS (`ais_data_large.csv`)
L'AIS (Automatic Identification System) permet de suivre la position et le statut de navigation des navires.
"""))

cells.append(nbf.v4.new_code_cell("""display(ais_df.info())
display(ais_df.head())
"""))

cells.append(nbf.v4.new_code_cell("""# Répartition des statuts de navigation
plt.figure(figsize=(10, 5))
sns.countplot(data=ais_df, y='status', order=ais_df['status'].value_counts().index, palette='viridis')
plt.title('Statuts de navigation AIS')
plt.show()
"""))

# Anomalies EDA
cells.append(nbf.v4.new_markdown_cell("""## 4. Analyse des Anomalies détectées (`anomalies_large.csv`)
Ceci est une liste d'anomalies déjà identifiées par le système de renseignement. Analysons les types d'anomalies les plus fréquents.
"""))

cells.append(nbf.v4.new_code_cell("""display(anomalies_df.info())
display(anomalies_df.head())
"""))

cells.append(nbf.v4.new_code_cell("""# Distribution des types d'anomalies
plt.figure(figsize=(8, 5))
sns.countplot(data=anomalies_df, y='type', order=anomalies_df['type'].value_counts().index, palette='Reds_r')
plt.title('Types d\\'anomalies')
plt.show()
"""))

nb['cells'] = cells

with open('analyse_generalisation.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook analyse_generalisation.ipynb créé avec succès !")
