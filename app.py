from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
current_id = 1


# CREATE
@app.route('/students', methods=['POST'])
def create_student():
    global current_id

    data = request.get_json() or {}
    name = data.get("name")

    if not name:
        return jsonify({"error": "Name required"}), 400

    student = {
        "id": current_id,
        "name": name
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201


# GET ALL
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# GET ONE
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student), 200

    return jsonify({"error": "Not found"}), 404


# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json() or {}
    name = data.get("name")

    for student in students:
        if student["id"] == id:
            student["name"] = name
            return jsonify(student), 200

    return jsonify({"error": "Not found"}), 404


# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return jsonify({"message": "Deleted"}), 200


# HEALTH CHECK (IMPORTANT FOR CI/CD)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)