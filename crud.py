from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
items = []
current_id = 1


# ---------------- CREATE ----------------
@app.route("/items", methods=["POST"])
def create_item():
    global current_id
    data = request.get_json()

    item = {
        "id": current_id,
        "name": data["name"],
        "value": data["value"]
    }
    items.append(item)
    current_id += 1

    return jsonify(item), 201


# ---------------- READ (ALL) ----------------
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


# ---------------- READ (ONE) ----------------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return {"error": "Item not found"}, 404


# ---------------- UPDATE ----------------
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["value"] = data.get("value", item["value"])
            return jsonify(item)
    return {"error": "Item not found"}, 404


# ---------------- DELETE ----------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
