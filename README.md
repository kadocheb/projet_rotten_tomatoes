# projet_rotten_tomatoes

Ce projet implémente un scraper pour extraire des données de films à partir du site Rotten Tomatoes et les stocker dans une base de données MongoDB. Ensuite, ces données sont utilisées pour générer différents tableaux de bord interactifs à l'aide de la bibliothèque Dash de Python.

## Prérequis

Allez dans le dossier rt_project.
Assurez-vous d'installer le pipenv cela peut prendre un petit temps:

```bash
pipenv install

#puis lorsque l'install est fini
pipenv shell
```

## Configuration de la connexion MongoDB

Avant d'exécuter le script de scraping, assurez-vous d'avoir une instance MongoDB en cours d'exécution. Vous pouvez configurer la connexion MongoDB dans le script tomatoes.py et dans le script principal app.py en modifiant la variable MONGODB_URI selon vos paramètres.


## Spider (Scraper)
Le script tomatoes.py utilise Scrapy pour extraire les données de films à partir de la page Rotten Tomatoes. Il nettoie les données et les stocke dans la base de données MongoDB. Vous pouvez l'exécuter avec la commande suivante :

```bash
scrapy crawl rotten_tomtoes
```

## Tableaux de bord Dash
Le script principal app.py utilise Dash pour créer trois onglets de tableau de bord interactifs :

1. Tableau des Données: Affiche les données brutes des films extraites de Rotten Tomatoes.

2. Scores d'Audience et de Critiques: Affiche des histogrammes des scores d'audience et de critiques.

3. Moyenne des Scores par Genre: Présente la moyenne des scores d'audience et de critiques par genre, ainsi qu'un histogramme du nombre de films par genre.

## Exécution de l'application Dash
Pour exécuter l'application Dash, utilisez la commande suivante :
```bash
python app.py
```
L'application sera accessible à l'adresse http://127.0.0.1:8050/ dans votre navigateur.

Assurez-vous que l'environnement virtuel dans lequel vous exécutez le script dispose de toutes les bibliothèques nécessaires installées (noramlement en respectant les prérequis cela doit bien marcher).
![image](https://github.com/kadocheb/projet_rotten_tomatoes/assets/134379752/61c999b2-c2c4-4cb3-be6d-f26fb261fb12)

