from blog import app

@app.route("/")
def homepage():
    return "<h1> Home Page </h1>"
