import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
st.title("Search and Operations of Sales")


# Initialize session state if not already set
if 'token' not in st.session_state:
    st.session_state['token'] = None


def login():
    """
    Displays a login form and handles authentication.

    Prompts the user to enter their email and password. Upon clicking the login button,
    it sends a POST request to the authentication endpoint. If successful, it stores the
    authentication token in the session state and reloads the page. Displays an error if the
    login attempt fails.
    """
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")
    if st.button("Login"):
        try:
            response = requests.post(f"{API_URL}/auth/login", json={"email": email, "password": password})
            response_data = response.json()
            if response.status_code == 200:
                st.success("Successfully logged in!")
                st.session_state['token'] = response_data['token']
                st.experimental_rerun()
            else:
                st.error(f"Error: {response_data['detail']}")
        except Exception as e:
            st.error(f"Error: {e}")


# Check if the user is logged in
if st.session_state['token']:
    headers = {"Authorization": f"Bearer {st.session_state['token']}"}

    action = st.sidebar.selectbox(
        "Select an action",
        [
            "Search sales by employee",
            "Search sales by product",
            "Search sales by Store",
            "Total and average sales by store",
            "Total and average sales product",
            "Total and average sales employee",
            "First row test"
        ]
    )

    def handle_response(response):
        """
        Handles the response from API requests.

        Args:
            response (requests.Response): The HTTP response object.

        Displays the response data as JSON if the request was successful. Otherwise,
        it shows an error message with the status code and error text.
        """
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    if action == "Search sales by employee":
        start_date = st.date_input("Start date").strftime("%Y-%m-%d")
        end_date = st.date_input("End date").strftime("%Y-%m-%d")
        key_employee = st.text_input("KeyEmployee")
        if st.button("Search sales by employee"):
            params = {
                "key_employee": key_employee,
                "start_date": start_date,
                "end_date": end_date
            }
            response = requests.get(f"{API_URL}/sales/employee/", headers=headers, params=params)
            handle_response(response)

    elif action == "Search sales by product":
        start_date = st.date_input("Start date").strftime("%Y-%m-%d")
        end_date = st.date_input("End date").strftime("%Y-%m-%d")
        key_product = st.text_input("KeyProduct")
        if st.button("Search sales by product"):
            params = {
                "key_product": key_product,
                "start_date": start_date,
                "end_date": end_date
            }
            response = requests.get(f"{API_URL}/sales/product/", headers=headers, params=params)
            handle_response(response)

    elif action == "Search sales by Store":
        start_date = st.date_input("Start date").strftime("%Y-%m-%d")
        end_date = st.date_input("End date").strftime("%Y-%m-%d")
        key_store = st.text_input("KeyStore")
        if st.button("Search sales by Store"):
            params = {
                "key_store": key_store,
                "start_date": start_date,
                "end_date": end_date
            }
            response = requests.get(f"{API_URL}/sales/store/", headers=headers, params=params)
            handle_response(response)

    elif action == "Total and average sales by store":
        key_store = st.text_input("KeyStore")
        if st.button("Total and average sales by store"):
            params = {"key_store": key_store}
            response = requests.get(f"{API_URL}/sales/store/total_avg/", headers=headers, params=params)
            handle_response(response)

    elif action == "Total and average sales product":
        key_product = st.text_input("KeyProduct")
        if st.button("Total and average sales product"):
            params = {"key_product": key_product}
            response = requests.get(f"{API_URL}/sales/product/total_avg/", headers=headers, params=params)
            handle_response(response)

    elif action == "Total and average sales employee":
        key_employee = st.text_input("KeyEmployee")
        if st.button("Total and average sales employee"):
            params = {"key_employee": key_employee}
            response = requests.get(f"{API_URL}/sales/employee/total_avg/", headers=headers, params=params)
            handle_response(response)

    elif action == "First row test":
        if st.button("First row test"):
            response = requests.get(f"{API_URL}/sales/first_record/", headers=headers)
            handle_response(response)
else:
    login()
    st.warning("Login with your credentials please")
