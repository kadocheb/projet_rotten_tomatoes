# projet_rotten_tomatoes

Ce projet implémente un scraper pour extraire des données de films à partir du site Rotten Tomatoes et les stocker dans une base de données MongoDB. Ensuite, ces données sont utilisées pour générer différents tableaux de bord interactifs à l'aide de la bibliothèque Dash de Python.

## Prérequis

Assurez-vous d'installer les bibliothèques nécessaires avant d'exécuter le projet. Vous pouvez le faire en exécutant la commande suivante :

```bash
pip install pymongo dash plotly scrapy
```

## Configuration de la connexion MongoDB

Avant d'exécuter le script de scraping, assurez-vous d'avoir une instance MongoDB en cours d'exécution. Vous pouvez configurer la connexion MongoDB dans le script spider.py et dans le script principal dashboard.py en modifiant la variable MONGODB_URI selon vos paramètres.


## Spider (Scraper)
Le script rt_spider.py utilise Scrapy pour extraire les données de films à partir de la page Rotten Tomatoes. Il nettoie les données et les stocke dans la base de données MongoDB. Vous pouvez l'exécuter avec la commande suivante :

```bash
scrapy crawl rotten_tomtoes
```

## Tableaux de bord Dash
Le script principal dashboard.py utilise Dash pour créer trois onglets de tableau de bord interactifs :

1. Tableau des Données: Affiche les données brutes des films extraites de Rotten Tomatoes.

2. Scores d'Audience et de Critiques: Affiche des histogrammes des scores d'audience et de critiques.

3. Moyenne des Scores par Genre: Présente la moyenne des scores d'audience et de critiques par genre, ainsi qu'un histogramme du nombre de films par genre.

## Exécution de l'application Dash
Pour exécuter l'application Dash, utilisez la commande suivante :
```bash
python run.py
```
L'application sera accessible à l'adresse http://127.0.0.1:8050/ dans votre navigateur.

Assurez-vous que l'environnement dans lequel vous exécutez le script dispose de toutes les bibliothèques nécessaires installées.
