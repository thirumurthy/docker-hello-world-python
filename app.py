from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return {"result":"Hello World from Python","author":"Thirumurthy","type":"Docker KSS-1"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
