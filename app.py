from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>My Flask UI</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #74ebd5, #ACB6E5);
            color: #333;
            text-align: center;
            padding-top: 100px;
          }
          h1 {
            color: #2c3e50;
            font-size: 3em;
            margin-bottom: 20px;
          }
          p {
            font-size: 1.2em;
            background-color: rgba(255,255,255,0.8);
            display: inline-block;
            padding: 10px 20px;
            border-radius: 8px;
          }
          .button {
            margin-top: 30px;
            padding: 12px 25px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1em;
            cursor: pointer;
            text-decoration: none;
          }
          .button:hover {
            background-color: #2980b9;
          }
        </style>
      </head>
      <body>
        <h1>🚀 Hello, this is your UI!</h1>
        <p>Welcome to the app running in your browser.</p>
        <a href="/" class="button">Refresh Page</a>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
