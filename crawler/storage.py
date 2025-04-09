import json
import os

DB_FILE = "database.json"

def init_db():
    """Initialize the database file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as db_file:
            json.dump({"pages": []}, db_file)

def save_to_db(data):
    """Save a new page to the database."""
    with open(DB_FILE, "r") as db_file:
        db = json.load(db_file)

    # Check if URL already exists
    if any(page["url"] == data["url"] for page in db["pages"]):
        print(f"URL already exists: {data['url']}")
        return

    db["pages"].append(data)

    with open(DB_FILE, "w") as db_file:
        json.dump(db, db_file, indent=4)

def get_all_pages():
    """Retrieve all pages from the database."""
    with open(DB_FILE, "r") as db_file:
        db = json.load(db_file)
    return db["pages"]