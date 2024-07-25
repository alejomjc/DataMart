"""
This module sets up and configures the FastAPI application, including middleware for authentication
and routes for various functionalities.

The main components are:
- FastAPI app initialization with custom settings.
- Middleware for handling authentication and authorization.
- Custom endpoint for retrieving the OpenAPI schema.
- Inclusion of authentication and sales routers.
"""

from fastapi import FastAPI, Request, HTTPException

from app.routers import auth, sales
from app.routers.utils import get_openapi_schema
from firebase_config import verify_token_local

app = FastAPI(
    title="Search and Operations of Sales",
    docs_url="/docs"
)


app.openapi_schema = get_openapi_schema()

excluded_paths = ["/auth/login", "/docs", "/openapi.json"]


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """
    Middleware to handle authentication by checking the Authorization header.

    This middleware extracts the JWT token from the Authorization header,
    verifies it, and attaches the decoded token data to the request state.
    If the token is missing or invalid, it raises an HTTP 401 Unauthorized error.

    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The function to call for the next middleware or endpoint.

    Raises:
        HTTPException: If the token is invalid or missing.

    Returns:
        Response: The HTTP response after processing the request.
    """
    if request.url.path not in excluded_paths:
        try:
            token = request.headers.get("Authorization").split("Bearer ")[1]
            decoded_token = verify_token_local(token)
            request.state.user = decoded_token
        except  Exception as exc:
            raise HTTPException(status_code=401, detail='Invalid or missing credentials') from exc

    response = await call_next(request)
    return response


@app.get("/openapi.json")
async def openapi():
    """
    Endpoint to retrieve the OpenAPI schema for the FastAPI application.

    Returns:
        dict: The OpenAPI schema in JSON format.
    """
    return app.openapi()


app.include_router(auth.router, prefix="/auth")
app.include_router(sales.router, prefix="/sales")
