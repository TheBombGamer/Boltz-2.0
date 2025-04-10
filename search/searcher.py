from crawler.storage import get_all_pages
from search.ranker import rank_results

def perform_search(query):
    
    pages = get_all_pages()
    results = []

    for page in pages:
        if query.lower() in page["content"].lower():
            results.append({
                "title": page["title"],
                "url": page["url"],
                "content": page["content"]
            })
            
    ranked_results = rank_results(query, results)
    return ranked_results
