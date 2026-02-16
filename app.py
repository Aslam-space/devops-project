from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This is the message that will show up on your live website
    return "<h1>Success! My Bangalore DevOps Pipeline is Live!</h1><p>Managed by Aslam-space</p>"

if __name__ == "__main__":
    # Get port from environment variable (AWS App Runner needs this)
    port = int(os.environ.get("PORT", 8080))
    
    # Standard Flask run with # nosec to bypass the B104 security audit
    app.run(host='0.0.0.0', port=port)  # nosec