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


# Description technique
## Scrapy
Le spider tomatoes.py est un script Python conçu pour le web scraping, utilisant le framework Scrapy. L'objectif principal de ce spider est d'extraire des informations spécifiques sur les films à partir du site web Rotten Tomatoes, puis de les stocker dans une base de données MongoDB. Voici une description technique détaillée de son fonctionnement :

  -Initialisation et Configuration :
Le spider est configuré pour se connecter à une instance MongoDB locale via l'URI spécifié.
Une base de données MongoDB est sélectionnée pour stocker les données des films.

  -Définition de la classe du Spider :
La classe RottenTomatoesSpider est définie, héritant des fonctionnalités de base fournies par Scrapy.
Les URLs de départ pour le scraping sont spécifiés dans la liste start_urls.
Un délai de téléchargement est défini pour éviter d'engorger le site web cible.

  -Méthode de Parsage :
La méthode parse est définie pour extraire les informations des pages web téléchargées.
Les données des films sont extraites en utilisant des sélecteurs CSS pour identifier les éléments HTML pertinents.
Pour chaque film extrait, un objet scrapy.Request est créé pour suivre le lien vers sa page individuelle, où des informations supplémentaires peuvent être obtenues.
Les données extraites sont nettoyées et transmises à la méthode parse_individual_page.

  -Méthode de Parsage de la Page Individuelle :
La méthode parse_individual_page est responsable de l'extraction des informations supplémentaires à partir des pages individuelles des films.
Les données extraites sont stockées dans un dictionnaire Python.

  -Stockage des Données dans MongoDB :
Les données extraites sont stockées dans une collection MongoDB appelée movies.
Chaque film est enregistré en tant que document JSON dans la collection.

  -Nettoyage de Texte :
La méthode clean_text est définie pour nettoyer les chaînes de texte extraites en supprimant les espaces blancs inutiles et les caractères spéciaux.

## Dashboard
Le dashboard Dash est une autre partie du script qui utilise les données extraites par le spider pour générer des visualisations interactives. Voici une description technique de son fonctionnement :

  -Initialisation et Configuration :
Le script se connecte à la même base de données MongoDB pour récupérer les données des films extraites par le spider.

  -Récupération des Données :
Les données des films sont récupérées à partir de la collection MongoDB movies.
Elles sont triées par score d'audience et de critiques dans un ordre décroissant.

  -Création des Visualisations :
Des visualisations telles que des histogrammes et des graphiques de barres sont générées à l'aide de la bibliothèque Plotly.
Les visualisations comprennent des histogrammes des scores d'audience et de critiques, un graphique de barres montrant la moyenne des scores par genre, et un histogramme du nombre de films par genre.

  -Interface Utilisateur :
L'interface utilisateur est créée à l'aide de la bibliothèque Dash, organisée en onglets pour permettre une navigation facile entre les différentes visualisations.

  -Exécution de l'Application Dash :
L'application Dash est exécutée, permettant aux utilisateurs d'interagir avec les visualisations à travers un serveur web local.

## Difficulté
La dockerisation de l'application, initialement configurée individuellement, a été entravée par un problème crucial : l'incapacité à se connecter à MongoDB, entraînant l'échec de l'exécution globale de l'application. Cette problématique a mis en lumière deux axes d'amélioration majeurs.

Premièrement, résoudre le problème de connexion à MongoDB dans l'environnement Docker est impératif pour assurer le bon fonctionnement de l'application conteneurisée. Cela nécessite une configuration appropriée des paramètres de connexion dans le conteneur Docker, en tenant compte des différences d'environnement entre le développement local et l'exécution dans un conteneur.

Deuxièmement, pour enrichir l'application, l'idée de scraper davantage de données en exploitant la fonctionnalité "suite" du site web pour afficher de nouveaux films est judicieuse. Cela permettrait d'élargir la base de données avec plus de films, améliorant ainsi la richesse des informations disponibles pour les utilisateurs du tableau de bord.

Pour mettre en œuvre ces améliorations, il est nécessaire de revisiter la configuration Docker pour garantir la connectivité à MongoDB, tout en ajustant le spider pour qu'il puisse parcourir les pages suivantes du site web et extraire les données supplémentaires. Une approche itérative, avec des tests fréquents pour s'assurer du bon fonctionnement à chaque étape, est recommandée pour garantir le succès de ces améliorations.
