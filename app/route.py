from flask import Blueprint, render_template, request
from search.searcher import perform_search

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_bp.route("/search", methods=["POST"])
def search():
    query = request.form.get("query", "")
    results = perform_search(query)
    return render_template("results.html", query=query, results=results)
