import scrapy
import pymongo

# Configurer la connexion MongoDB
MONGODB_URI = 'mongodb://localhost:27017/'
MONGODB_DB = 'rotten_tomatoes_db'

# Initialiser la connexion MongoDB
client = pymongo.MongoClient(MONGODB_URI)
db = client[MONGODB_DB]

class RottenTomatoesSpider(scrapy.Spider):
    name = "rotten_tomatoes"
    start_urls = start_urls = ['https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=5']
    download_delay = 1


    def parse(self, response):
        # Sélectionnez tous les éléments de film sur la page
        films = response.css('div.flex-container')

        for film in films:
            # Extrayez le titre
            title = self.clean_text(film.css('span[data-qa="discovery-media-list-item-title"]::text').get())
            
            # Extrayez la date de début
            date = self.clean_text(film.css('span[data-qa="discovery-media-list-item-start-date"]::text').get())

            # Extrayez les scores
            audiencescore = film.css('score-pairs-deprecated::attr(audiencescore)').get()
            criticsscore = film.css('score-pairs-deprecated::attr(criticsscore)').get()

            # Récupérez le lien vers la page individuelle du film
            film_link = film.css('a[data-qa="discovery-media-list-item-caption"]::attr(href)').get()

            # Suivez le lien vers la page individuelle du film
            yield scrapy.Request(
                url=response.urljoin(film_link),
                callback=self.parse_individual_page,
                meta={
                    'title': title,
                    'date': date,
                    'audiencescore': audiencescore,
                    'criticsscore': criticsscore,
                }
            )

    def parse_individual_page(self, response):
        # Extrayez le genre depuis la page individuelle du film
        genre = self.clean_text(response.css('span.genre::text').get().strip())

        title = response.meta['title']
        date = response.meta['date']
        audiencescore = response.meta['audiencescore']
        criticsscore = response.meta['criticsscore']

         # Stocker les données dans MongoDB
        movie_data = {
            'Title': title,
            'Date': date,
            'Audience Score': audiencescore,
            'Critics Score': criticsscore,
            'Genre': genre,
            }

        # Insérer les données dans la collection 'movies'
        db.movies.insert_one(movie_data)

        yield movie_data


    def clean_text(self, text):
        # Exemple de nettoyage du texte sans utiliser re
        if text:
            # Supprimer les espaces blancs inutiles et caractères spéciaux
            cleaned_text = ' '.join(text.split()).strip()
            return cleaned_text
        else:
            return None
        

