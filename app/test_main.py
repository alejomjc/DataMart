from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_login():
    """
    Test the login endpoint to ensure it returns a valid JWT token.

    Sends a POST request to the /auth/login endpoint with test credentials and
    verifies that the response status code is 200 and contains a token.
    The token is then stored globally for use in subsequent tests.
    """
    response = client.post("/auth/login", json={"email": "test@mail.com", "password": "Test123"})
    assert response.status_code == 200
    assert "token" in response.json()
    global token
    token = response.json()["token"]


def test_get_sales_by_employee():
    """
    Test retrieving sales data by employee.

    Sends a GET request to the /sales/employee/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and contains at least one record.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/employee/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_employee": "1|343", "start_date": "2023-11-01", "end_date": "2023-11-03"})
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_sales_by_product():
    """
    Test retrieving sales data by product.

    Sends a GET request to the /sales/product/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and contains at least one record.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/product/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_product": "1|44733", "start_date": "2023-11-01", "end_date": "2023-11-03"})
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_sales_by_store():
    """
    Test retrieving sales data by store.

    Sends a GET request to the /sales/store/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and contains at least one record.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/store/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_store": "1|023", "start_date": "2023-11-01", "end_date": "2023-11-03"})
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_total_avg_sales_by_store():
    """
    Test retrieving total and average sales data by store.

    Sends a GET request to the /sales/store/total_avg/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and the response is a dictionary.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/store/total_avg/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_store": "1|023"})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_total_avg_sales_by_product():
    """
    Test retrieving total and average sales data by product.

    Sends a GET request to the /sales/product/total_avg/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and the response is a dictionary.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/product/total_avg/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_product": "1|44733"})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_total_avg_sales_by_employee():
    """
    Test retrieving total and average sales data by employee.

    Sends a GET request to the /sales/employee/total_avg/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and the response is a dictionary.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/employee/total_avg/", headers={"Authorization": f"Bearer {token}"},
                          params={"key_employee": "1|343"})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_first_record():
    """
    Test retrieving the first record in the dataset.

    Sends a GET request to the /sales/first_record/ endpoint with a valid JWT token
    and verifies that the response status code is 200 and the response is a dictionary.

    Assumes that the test login has already been performed and the token is valid.
    """
    response = client.get("/sales/first_record/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
