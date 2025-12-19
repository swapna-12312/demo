from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
