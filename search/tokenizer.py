import re

def tokenize(text):
    """
    Tokenizes and normalizes the input text.
    
    Args:
        text (str): The text to tokenize.
    
    Returns:
        list: A list of normalized tokens (words).
    """
    
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)
    
    tokens = text.split()
    
    return tokens


def query_to_tokens(query):
    """
    Tokenizes a user's query.
    
    Args:
        query (str): The search query entered by the user.
    
    Returns:
        list: A list of normalized tokens from the query.
    """
    return tokenize(query)
