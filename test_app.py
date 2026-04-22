import requests

BASE_URL = "http://localhost:3000"

def test_health():
    res = requests.get(f"{BASE_URL}/health")
    assert res.status_code == 200

def test_create_student():
    res = requests.post(f"{BASE_URL}/students", json={"name": "Nikhil"})
    assert res.status_code == 201

def test_get_students():
    res = requests.get(f"{BASE_URL}/students")
    assert res.status_code == 200