from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

import random

@app.route("/")

def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tmw_movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"  #content = content + <h1>...
    content += "</ul>"
    content += "<h2>Tomorrow's Movie</h2>"
    content += "<ul>"
    content += "<li>" + tmw_movie + "</li>"
    content += "</ul>"


    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ["The Fellowship of the Ring", "The Two Towers", "The Return of the King",
    "The Hobbit: An Unexpected Journey", "The Hobbit: The Desolation of Smaug",
    "The Hobbit: The Battle of the Five Armies"
    ]
    # TODO: randomly choose one of the movies, and return it
    random_movie = random.choice(movies)
    return random_movie


app.run()
