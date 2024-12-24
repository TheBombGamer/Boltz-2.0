def rank_results(query, results):
    """
    Rank search results based on relevance to the query.
    
    Args:
        query (str): The search query entered by the user.
        results (list): A list of result dictionaries, each containing 'title', 'url', and 'content'.
    
    Returns:
        list: Ranked results sorted by relevance.
    """
    query = query.lower()
    
    def relevance_score(result):
        """Calculate relevance score based on the query frequency in the content."""
        content = result["content"].lower()
        return content.count(query)
    
    # Sort results by relevance score (higher is better)
    ranked_results = sorted(results, key=relevance_score, reverse=True)
    return ranked_results
