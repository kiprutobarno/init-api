import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to the API</h1>"


@app.route("/api/v1/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/api/v1/books/<int:id>", methods=["GET"])
def get_book(id):

    result = []

    for book in books:
        if book['id'] == id:
            print(book)
            result.append(book)
    if len(result) == 0:
        return jsonify({"status": 404, "message": "No book with id "+str(id)}), 404
    return jsonify(result)


app.run()
