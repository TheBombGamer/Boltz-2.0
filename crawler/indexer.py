from crawler.crawler import crawl
from crawler.storage import init_db, save_to_db, get_all_pages

def main():
    
    init_db()

    start_url = input("Enter the URL to start crawling: ")

    page_data = crawl(start_url)

    if page_data:
        save_to_db(page_data)
        print(f"Crawled and saved: {page_data['url']}")
    else:
        print("Failed to crawl the URL.")

    print("Crawled pages in the database:")
    for page in get_all_pages():
        print(f"URL: {page['url']}, Title: {page['title']}")

if __name__ == "__main__":
    main()