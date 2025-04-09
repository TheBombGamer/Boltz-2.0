import requests
from bs4 import BeautifulSoup

def crawl(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        content = soup.get_text()
        return {"url": url, "title": title, "content": content}
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return None