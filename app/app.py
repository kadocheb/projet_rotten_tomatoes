from pymongo import MongoClient
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px



# Configurer la connexion MongoDB pour Dash
MONGODB_URI = 'mongodb://localhost:27017/'
MONGODB_DB = 'rotten_tomatoes_db'

# Initialiser la connexion MongoDB pour Dash
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB]


# Récupérer les données depuis MongoDB
movies_data = list(db.movies.find())

# Trier les données par audience score et critics score (ordre décroissant)
movies_data.sort(key=lambda x: x['Audience Score'], reverse=True)
movies_data.sort(key=lambda x: x['Critics Score'], reverse=True)

# Créer un histogramme des scores d'audience
fig_audience = px.histogram(movies_data, x="Audience Score", title="Audience Score Distribution")

# Créer un histogramme des scores des critiques
fig_critics = px.histogram(movies_data, x="Critics Score", title="Critics Score Distribution")

# Créer une application Dash
app = dash.Dash(__name__)





# Calculer la moyenne des notes par genre
avg_scores_by_genre = {}
genres_set = set()

# Parcourir les films et ajouter chaque genre à l'ensemble
for movie in movies_data:
    # Normaliser les noms de genres en minuscules et supprimer les espaces blancs inutiles
    genres = [genre.strip().lower() for genre in movie['Genre'].split(',')]
    
    for genre in genres:
        # Ajouter le genre à l'ensemble global
        genres_set.add(genre)
        
        # Ajouter le film aux genres pour la moyenne
        if genre not in avg_scores_by_genre:
            avg_scores_by_genre[genre] = {
                'Audience Scores': [],
                'Critics Scores': [],
            }
        
        # Ajouter les scores du film aux scores du genre
        audience_score = float(movie['Audience Score']) if movie['Audience Score'] else None
        critics_score = float(movie['Critics Score']) if movie['Critics Score'] else None
        
        avg_scores_by_genre[genre]['Audience Scores'].append(audience_score)
        avg_scores_by_genre[genre]['Critics Scores'].append(critics_score)

# Calculer la moyenne des notes par genre
for genre in genres_set:
    audience_scores = [score for score in avg_scores_by_genre[genre]['Audience Scores'] if score is not None]
    critics_scores = [score for score in avg_scores_by_genre[genre]['Critics Scores'] if score is not None]
    
    avg_audience_score = sum(audience_scores) / len(audience_scores) if audience_scores else 0
    avg_critics_score = sum(critics_scores) / len(critics_scores) if critics_scores else 0
    
    avg_scores_by_genre[genre]['Average Audience Score'] = avg_audience_score
    avg_scores_by_genre[genre]['Average Critics Score'] = avg_critics_score

# Trier les genres par ordre décroissant de la moyenne des scores d'audience
sorted_genres = sorted(genres_set, key=lambda genre: avg_scores_by_genre[genre]['Average Audience Score'], reverse=True)

# Créer un graphique de barres pour la moyenne des notes par genre
fig_avg_scores = px.bar(x=sorted_genres,
                        y=[avg_scores_by_genre[genre]['Average Audience Score'] for genre in sorted_genres],
                        color_discrete_sequence=['blue'],  # Couleur pour les scores d'audience
                        title='Average Audience Score by Genre',
                        labels={'x': 'Genre', 'y': 'Average Audience Score'},
                        text=[f'Audience Score: {avg:.2f}' for avg in [avg_scores_by_genre[genre]['Average Audience Score'] for genre in sorted_genres]])

# Ajouter un autre graphique de barres pour les scores de critiques
fig_avg_scores.add_trace(px.bar(x=sorted_genres,
                                y=[avg_scores_by_genre[genre]['Average Critics Score'] for genre in sorted_genres],
                                color_discrete_sequence=['red'],  # Couleur pour les scores de critiques
                                title='Average Critics Score by Genre',
                                labels={'x': 'Genre', 'y': 'Average Critics Score'},
                                text=[f'Critics Score: {avg:.2f}' for avg in [avg_scores_by_genre[genre]['Average Critics Score'] for genre in sorted_genres]]).data[0])

# Mettre à jour l'ordre des étiquettes sur l'axe x pour les deux graphiques
fig_avg_scores.update_xaxes(categoryorder='total descending')





# Créer un ensemble pour stocker tous les genres uniques
all_genres_set = set()

# Parcourir les films et ajouter chaque genre à l'ensemble
for movie in movies_data:
    # Normaliser les noms de genres en minuscules et supprimer les espaces blancs inutiles
    genres = [genre.strip().lower() for genre in movie['Genre'].split(',')]
    all_genres_set.update(genres)

# Compter le nombre de films par genre
genre_counts = {genre: sum(genre in movie['Genre'].lower() for movie in movies_data) for genre in all_genres_set}

# Trier les genres par ordre décroissant du nombre de films
sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

# Créer un histogramme du nombre de films par genre
fig_genre_count = px.bar(x=[genre[0] for genre in sorted_genres], y=[genre[1] for genre in sorted_genres],
                         title='Number of Movies per Genre',
                         labels={'x': 'Genre', 'y': 'Number of Movies'})







# Définir la mise en page de l'application avec des onglets
app.layout = html.Div(children=[
    dcc.Tabs([
        dcc.Tab(label='Tableau des Données', children=[
            html.H1(children='Rotten Tomatoes Dashboard - Tableau des Données'),

            html.Table(children=[
                html.Tr(children=[
                    html.Th('Title'),
                    html.Th('Date'),
                    html.Th('Audience Score'),
                    html.Th('Critics Score'),
                    html.Th('Genre'),
                ])
            ] + [
                html.Tr(children=[
                    html.Td(movie['Title']),
                    html.Td(movie['Date']),
                    html.Td(movie['Audience Score']),
                    html.Td(movie['Critics Score']),
                    html.Td(movie['Genre']),
                ]) for movie in movies_data
            ])
        ]),

        dcc.Tab(label='Scores d\'Audience et de Critiques', children=[
            html.H1(children='Rotten Tomatoes Dashboard - Scores d\'Audience et de Critiques'),

            dcc.Graph(
                id='audience_score_histogram',
                figure=fig_audience
            ),

            dcc.Graph(
                id='critics_score_histogram',
                figure=fig_critics
            ),
        ]),

        dcc.Tab(label='Moyenne des Scores par Genre', children=[
            html.H1(children='Rotten Tomatoes Dashboard - Moyenne des Scores par Genre'),

            dcc.Graph(
                id='average_scores_by_genre',
                figure=fig_avg_scores
            ),

            dcc.Graph(
                id='genre_count_histogram',
                figure=fig_genre_count
            ),
        ]),
    ]),
])




# Exécuter l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
