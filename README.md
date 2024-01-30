# projet_rotten_tomatoes

Ce projet implémente un scraper pour extraire des données de films à partir du site Rotten Tomatoes et les stocker dans une base de données MongoDB. Ensuite, ces données sont utilisées pour générer différents tableaux de bord interactifs à l'aide de la bibliothèque Dash de Python.

## Prérequis

Assurez-vous d'installer les bibliothèques nécessaires avant d'exécuter le projet. Vous pouvez le faire en exécutant la commande suivante :

```bash
pip install pymongo dash plotly scrapy


## Configuration de la connexion MongoDB

Avant d'exécuter le script de scraping, assurez-vous d'avoir une instance MongoDB en cours d'exécution. Vous pouvez configurer la connexion MongoDB dans le script spider.py et dans le script principal dashboard.py en modifiant la variable MONGODB_URI selon vos paramètres.
