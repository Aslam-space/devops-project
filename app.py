from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This message proves your deployment worked
    return "<h1>Success! My DevOps Pipeline is Live!</h1><p>Repo: devops-project | Managed by Aslam-space</p>"

if __name__ == "__main__":
    # AWS App Runner will inject the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    
    # We use 0.0.0.0 so the container can accept outside traffic
    app.run(host='0.0.0.0', port=port)