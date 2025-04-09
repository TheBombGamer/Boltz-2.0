from flask import Blueprint, render_template, request, jsonify
from search.searcher import perform_search
from crawler.crawler import crawl
from crawler.storage import save_to_db, get_all_pages

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_bp.route("/search", methods=["POST"])
def search():
    query = request.form.get("query", "")
    results = perform_search(query)
    return render_template("results.html", query=query, results=results)

@main_bp.route("/crawl", methods=["POST"])
def crawl_url():
    """Crawl a URL and save the result."""
    url = request.form.get("url", "")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    page_data = crawl(url)
    if page_data:
        save_to_db(page_data)
        return jsonify({"message": "Crawled and saved", "data": page_data}), 200
    else:
        return jsonify({"error": "Failed to crawl the URL"}), 500

@main_bp.route("/pages", methods=["GET"])
def get_pages():
    """Retrieve all crawled pages."""
    pages = get_all_pages()
    return render_template("pages.html", pages=pages)