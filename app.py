from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This is the message that will show up on your live website
    return "<h1>Success! My Bangalore DevOps Pipeline is Live!</h1><p>Deployed by Aslam-space</p>"

if __name__ == "__main__":
    # Get port from environment variable (AWS App Runner sets this automatically)
    port = int(os.environ.get("PORT", 8080))
    
    # '# nosec' tells the security scanner to ignore the 0.0.0.0 binding warning
    app.run(host='0.0.0.0', port=port)  # nosec