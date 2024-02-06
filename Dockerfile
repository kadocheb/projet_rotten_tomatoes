# Utilisez une image de base appropriée avec Python
FROM python:3.8

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app
WORKDIR /app

# Installez les dépendances
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# Commande pour lancer le spider une fois
CMD ["pipenv", "run", "scrapy", "crawl", "rotten_tomatoes", "&&", "python", "run.py"]