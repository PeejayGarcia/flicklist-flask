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
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"
    error = request.args.get('error', False)
    content = page_header + edit_header + add_form + crossoff_form + page_footer
    if not error:

    # build the response string
        
        return content
    
    error_element =  "<p style='color:red;'>{}</p>".format(error)
    return content + error_element


app.run()