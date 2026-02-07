# API Case Study
# After watching the video, create a CRUD API for a Book instead of a Drink in the video example above.  
# The Book model should have the following parameters:
# id
# book_name
# author
# publisher

from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------
# database
# -----------------------------
books = [
    {"id": 1, "book_name": "1984", "author": "George Orwell", "publisher": "Secker & Warburg"},
    {"id": 2, "book_name": "Dune", "author": "Frank Herbert", "publisher": "Chilton Books"}
]

# -----------------------------
# GET all books
# -----------------------------
@app.route('/allbooks', methods=['GET'])
def get_books():
    return jsonify(books)

# -----------------------------
# GET book by ID
# -----------------------------
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# -----------------------------
# POST create a new book 
# -----------------------------
@app.route('/postbooks', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": data["id"],
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# -----------------------------
# DELETE a book
# -----------------------------
@app.route('/delbooks/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

# -----------------------------
# Run the server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
