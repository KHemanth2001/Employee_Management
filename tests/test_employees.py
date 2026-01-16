def test_create_employee(client, auth_headers):
    response = client.post(
        "/api/employees",
        headers=auth_headers,
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
    )
    assert response.status_code == 201


def test_create_employee_duplicate_email(client, auth_headers):
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "department": "HR",
        "role": "Manager"
    }

    client.post("/api/employees", headers=auth_headers, json=payload)
    response = client.post("/api/employees", headers=auth_headers, json=payload)

    assert response.status_code == 400


def test_get_all_employees(client, auth_headers):
    response = client.get("/api/employees", headers=auth_headers)
    assert response.status_code == 200
    assert "items" in response.json()
    assert "total" in response.json()


def test_get_employee_by_id(client, auth_headers):
    create = client.post(
        "/api/employees",
        headers=auth_headers,
        json={
            "name": "Mark",
            "email": "mark@example.com"
        }
    )

    emp_id = 1
    response = client.get(f"/api/employees/{emp_id}", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["id"] == emp_id


def test_get_employee_not_found(client, auth_headers):
    response = client.get("/api/employees/999", headers=auth_headers)
    assert response.status_code == 404


def test_update_employee(client, auth_headers):
    client.post(
        "/api/employees",
        headers=auth_headers,
        json={
            "name": "Old Name",
            "email": "old@example.com"
        }
    )

    response = client.put(
        "/api/employees/1",
        headers=auth_headers,
        json={
            "name": "New Name",
            "email": "old@example.com"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "New Name"


def test_delete_employee(client, auth_headers):
    client.post(
        "/api/employees",
        headers=auth_headers,
        json={
            "name": "Delete Me",
            "email": "delete@example.com"
        }
    )

    response = client.delete("/api/employees/1", headers=auth_headers)
    assert response.status_code == 204


def test_unauthorized_access(client):
    response = client.get("/api/employees")
    assert response.status_code == 403 or response.status_code == 401


def test_create_employee_invalid_email(client, auth_headers):
    response = client.post(
        "/api/employees",
        headers=auth_headers,
        json={
            "name": "Invalid",
            "email": "not-an-email"
        }
    )
    assert response.status_code == 400
