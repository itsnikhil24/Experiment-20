import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


# HEALTH CHECK
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "OK"


# CREATE
def test_create_student(client):
    response = client.post("/students", json={"name": "Nikhil"})
    assert response.status_code == 201
    assert response.json["name"] == "Nikhil"


# GET ALL
def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json, list)


# GET ONE
def test_get_student(client):
    create_response = client.post("/students", json={"name": "Student-2"})
    student_id = create_response.json["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Student-2"


# UPDATE
def test_update_student(client):
    create_response = client.post("/students", json={"name": "Student-3"})
    student_id = create_response.json["id"]

    response = client.put(f"/students/{student_id}", json={"name": "Updated"})
    assert response.status_code == 200
    assert response.json["name"] == "Updated"


# DELETE
def test_delete_student(client):
    create_response = client.post("/students", json={"name": "Student-4"})
    student_id = create_response.json["id"]

    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 404