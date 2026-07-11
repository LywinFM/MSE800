import flask

app = flask.Flask (__name__)


@app.route ("/")
def hello_flask() -> str:
    return "<p>Hello, World!</p>"
