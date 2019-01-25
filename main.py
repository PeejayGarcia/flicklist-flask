from flask import Flask, request, redirect
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label>
            I want to add
            <input type="text" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""
# a form for crossing off watched movies

## TODO: We want to dynamically build the options using the current watchlist.
## Use an accumulator method to accumulate the options.
## options = "" and use a for loop to get each movie.
##

## TODO: Write a function that gets the current users watchlist.
## Right now, we don't have a databse, so we can pretten to get
## the watchlist by just returning a hardcoded list of movie titles.

def get_current_watchlist():
    return['The Fellowship of the Ring', 'The Two Towers', 'The Return of the King',
        'The Hobbit: An Unexpected Journey', 'The Hobbit: The Desolation of Smaug', 'The Hobbit: The Battle of the 5 Armies']


options = ""
for movie in get_current_watchlist():
    options += '<option value="{0}">{0}</option>'.format(movie)
    # 

crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(options)

def get_current_watchlist():
    # returns user's current watchlist--hard coded for now
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]

# a form for crossing off watched movies
# (first we build a dropdown from the current watchlist items)
crossoff_options = ""
for movie in get_current_watchlist():
    crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {0}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(crossoff_options)

# a list of movies that nobody should have to watch
terrible_movies = [
    "Gigli",
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives",
    "Starship Troopers"
]


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    if crossed_off_movie not in get_current_watchlist():
        # the user tried to cross off a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)

    # if we didn't redirect by now, then all is well
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
    content = page_header + "<p>" + confirmation + "</p>" + page_footer

    return content



@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    ## TODO: Validate that crossed_off_movie is in the current watchlist
    ## If it is, do what we're doing already.
    ## Else, send the meaningful error as a query parameter while
    ## redirecting back to /. (/?error=SOMEERRORSTRINGHERE)
    ## NOTE: Remember to escape the error message.
    print("Move:", movie)
    print("Crossed off movie:", crossed_off_movie)
    if crossed_off_movie in get_current_watchlist():            
        crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
        confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
        content = page_header + "<p>" + confirmation + "</p>" + page_footer

        return content
    error_url = "/?error={} isn't in your watchlist!".format(crossed_off_movie)
    error_url_escaped = cgi.escape(error_url)
    return redirect('/' + error_url)

@app.route("/add", methods=['POST'])
def add_movie():

    new_movie =cgi.escape(request.form['new-movie'])

    # TODO 
    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site

    # new_movie = request.form['new-movie']
    # TODO 
    # if the user typed nothing at all, redirect and tell them the error
    if (new_movie.strip() == ""):
        error = 'Please specify the name of the movie you want to add.'
        return redirect("/?error={}".format(error))
    # TODO 
    # if the user wants to add a terrible movie, redirect and tell them not to add it b/c it sucks
    if (new_movie in terrible_movies):
        error = "Trust me, you don't want to add '{}' to your Watchlist.".format(new_movie)
        return redirect("/?error=={}".format(error))
    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # if we have an error, make a <p> to display it
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''

    # combine all the pieces to build the content of our response
    main_content = edit_header + add_form + crossoff_form + error_element


    # build the response string
    content = page_header + main_content + page_footer

    return content
  
    error = request.args.get('error', False)
    content = page_header + edit_header + add_form + crossoff_form + page_footer
    if not error:

    # build the response string
        
        return content
    
    error_element =  "<p style='color:red;'>{}</p>".format(error)
    return content + error_element

app.run()