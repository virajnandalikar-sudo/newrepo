from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, this is your UI!</h1><p>Welcome to the app running in your browser.</p>"

if __name__ == "__main__":
    # Run on localhost:5000
    app.run(host="0.0.0.0", port=5001, debug=True)
