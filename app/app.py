from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/rotten_tomatoes_db"
mongo = PyMongo(app)

@app.route('/')
def index():
    films = list(mongo.db.films.find())
    return render_template('films.html', films=films)

@app.route('/api/films')
def films_api():
    films = list(mongo.db.films.find()) 
    return jsonify(films)


