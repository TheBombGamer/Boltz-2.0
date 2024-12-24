from crawler.storage import get_all_pages
from search.ranker import rank_results

def perform_search(query):
    """Search for pages containing the query and rank the results."""
    pages = get_all_pages()
    results = []

    for page in pages:
        if query.lower() in page["content"].lower():
            results.append({
                "title": page["title"],
                "url": page["url"],
                "content": page["content"]
            })
    
    # Rank the results
    ranked_results = rank_results(query, results)
    return ranked_results
