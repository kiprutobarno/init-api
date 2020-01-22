import flask
from flask import jsonify, request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to the API</h1>"


@app.route("/api/v1/books", methods=["GET"])
def get_books():
    conn = sqlite3.connect("books.db")
    conn.row_factory = dict_factory
    books = conn.cursor().execute('SELECT * FROM books;').fetchall()
    return jsonify(books)


@app.route("/api/v1/books/<string:author>", methods=["GET"])
def get_book_by_author(author):

    query = "SELECT * FROM books where author="+author
    conn = sqlite3.connect("books.db")
    conn.row_factory = dict_factory
    return jsonify(conn.cursor().execute(query).fetchall())


@app.route("/api/v1/books/<int:published>", methods=["GET"])
def get_book_by_published(published):

    query = "SELECT * FROM books where published="+str(published)
    conn = sqlite3.connect("books.db")
    return jsonify(conn.cursor().execute(query).fetchall())


app.run()
