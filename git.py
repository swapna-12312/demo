from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.get_json()
        return {"result": data["a"] + data["b"]}

    # GET request (for browser)
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return {"result": a + b}


if __name__ == "__main__":
    app.run(debug=True)
