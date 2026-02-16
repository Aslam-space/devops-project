from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Success! My Bangalore DevOps Pipeline is Live!</h1>"

if __name__ == "__main__":
    # AWS App Runner will provide the PORT automatically
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)