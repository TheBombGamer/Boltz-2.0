# run.py
from app import create_app
from crawler.storage import init_db

init_db()

app = create_app()
app2 = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    app2.run(host="0.0.0.0", port=3000, debug=True)