"""
This module defines the schema for login requests using Pydantic.
"""

from pydantic import BaseModel

class LoginSchema(BaseModel):
    """
    Schema for validating login requests.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for the user account.
    """

    email: str
    password: str

    class Config:
        """
        Configuration for the LoginSchema.

        Attributes:
            schema_extra (dict): Example data for the schema.
        """
        schema_extra = {
            "example": {
                "email": "test@mail.com",
                "password": "Test123"
            }
        }
