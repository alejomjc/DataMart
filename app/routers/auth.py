"""
This module contains the authentication routes for the FastAPI application.

It includes:
- A POST route for user login, which authenticates the user and returns a JWT token.
"""

from fastapi import APIRouter, HTTPException
from firebase_config import firebase_auth

from app.models import LoginSchema

router = APIRouter()


@router.post("/login")
def login(request: LoginSchema):
    """
    Authenticates a user and returns a token if the credentials are valid.

    Args:
        request (LoginSchema): The login request object containing email and password.

    Returns:
        dict: A dictionary containing the authentication token.

    Raises:
        HTTPException: If authentication fails or an error occurs.
    """
    try:
        user = firebase_auth.sign_in_with_email_and_password(request.email, request.password)
        return {"token": user['idToken']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
