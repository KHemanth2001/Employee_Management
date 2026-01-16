def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "newuser",
            "email": "new@example.com",
            "password": "secret123"
        }
    )
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"


def test_register_duplicate_user(client):
    client.post(
        "/auth/register",
        json={
            "username": "dupuser",
            "email": "dup@example.com",
            "password": "secret123"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "dupuser",
            "email": "dup@example.com",
            "password": "secret123"
        }
    )

    assert response.status_code == 400


def test_login_success(client):
    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "username": "loginuser",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid_credentials(client):
    response = client.post(
        "/auth/login",
        json={
            "username": "nouser",
            "password": "wrong"
        }
    )
    assert response.status_code == 401


def test_invalid_token(client):
    response = client.get(
        "/api/employees",
        headers={"Authorization": "Bearer invalidtoken"}
    )
    assert response.status_code == 401
