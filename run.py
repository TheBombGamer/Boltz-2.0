# run.py
from app import create_app
from crawler.storage import init_db

init_db()

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
