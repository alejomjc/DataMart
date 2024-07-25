# FastAPI and Streamlit with Firebase Integration

This project demonstrates how to use FastAPI and Streamlit with Firebase.

## Prerequisites

- Python 3.6+

## Local Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a .env file in the root directory and add your Firebase configuration:**

   ```sh
    FIREBASE_API_KEY=your_firebase_api_key
    FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
    FIREBASE_PROJECT_ID=your_firebase_project_id
    FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
    FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
    FIREBASE_APP_ID=your_firebase_app_id
    FIREBASE_MEASUREMENT_ID=your_firebase_measurement_id
    FIREBASE_DATABASE_URL=your_firebase_database_url
    FIREBASE_TYPE=service_account
    FIREBASE_PRIVATE_KEY_ID=your_private_key_id
    FIREBASE_PRIVATE_KEY=your_private_key
    FIREBASE_CLIENT_EMAIL=your_client_email
    FIREBASE_CLIENT_ID=your_client_id
    FIREBASE_AUTH_URI=your_auth_uri
    FIREBASE_TOKEN_URI=your_token_uri
    FIREBASE_AUTH_PROVIDER_CERT_URL=your_auth_provider_cert_url
    FIREBASE_CLIENT_CERT_URL=your_client_cert_url
   ```

5. **Run the FastAPI server:**

   ```sh
   uvicorn main:app --reload
   ```

5. **Run the Streamlit application:**

   ```sh
   streamlit run app.py
   ```   
