def rank_results(query, results):

    query = query.lower()
    
    def relevance_score(result):
        
        content = result["content"].lower()
        return content.count(query)
    
    ranked_results = sorted(results, key=relevance_score, reverse=True)
    return ranked_results
