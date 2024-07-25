"""
This module provides functions for validating dates and calculating sales metrics.

Functions:
    - validate_dates(start_date: str, end_date: str)
    -> tuple: Validates and parses the start and end dates.
    - calculate_totals_and_averages(filtered_df: pd.DataFrame)
    -> dict: Calculates total and average sales from a filtered DataFrame.
    - get_openapi_schema()
    -> generates the OpenAPI schema for the sales and authentication endpoints.
"""

from datetime import datetime

from fastapi import HTTPException
import pandas as pd


def validate_dates(start_date: str, end_date: str):
    """
    Validates and parses the start and end dates.

    Args:
        start_date (str): The start date in YYYY-MM-DD format.
        end_date (str): The end date in YYYY-MM-DD format.

    Returns:
        tuple: A tuple containing two datetime.date objects (start_date, end_date).

    Raises:
        HTTPException: If the date format is invalid.
    """
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail='Invalid date format. Use YYYY-MM-DD.') from exc
    return start_date_dt, end_date_dt


def calculate_totals_and_averages(filtered_df: pd.DataFrame) -> dict:
    """
    Calculates the total and average sales from a filtered DataFrame.

    Args:
        filtered_df (pd.DataFrame): A DataFrame containing sales data.

    Returns:
        dict: A dictionary with total and average sales formatted as strings.

    Raises:
        HTTPException: If no sales data is found in the DataFrame.
    """
    if len(filtered_df.columns) == 0:
        raise HTTPException(status_code=404, detail="No sales data found.")
    total_sales = filtered_df['Tickets'].apply(lambda x: x['NetAmount']).sum()
    average_sales = filtered_df['Tickets'].apply(lambda x: x['NetAmount']).mean()
    return {
        "total_sales": f"${total_sales:,.2f}",
        "average_sales": f"${average_sales:,.2f}"
    }


def get_openapi_schema():
    """
    Generates the OpenAPI schema for the sales and authentication endpoints.

    Returns:
        dict: The OpenAPI schema as a dictionary.
    """
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Search and Operations of Sales",
            "version": "1.0.0"
        },
        "paths": {
            "/sales/employee": {
                "get": {
                    "summary": "Get sales data by employee",
                    "description": "Retrieve sales data for a specific employee in a date range.",
                    "parameters": [
                        {
                            "name": "key_employee",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        },
                        {
                            "name": "start_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        },
                        {
                            "name": "end_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales found for the given employee and date range."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/product/": {
                "get": {
                    "summary": "Get sales data by product",
                    "description": "Retrieve sales for a specific product within a date range.",
                    "parameters": [
                        {
                            "name": "key_product",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        },
                        {
                            "name": "start_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        },
                        {
                            "name": "end_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales found for the given product and date range."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/store/": {
                "get": {
                    "summary": "Get sales data by store",
                    "description": "Retrieve sales data for a specific store within a date range.",
                    "parameters": [
                        {
                            "name": "key_store",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        },
                        {
                            "name": "start_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        },
                        {
                            "name": "end_date",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string",
                                "format": "date"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales data found for the given store and date range."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/store/total_avg/": {
                "get": {
                    "summary": "Get total and average sales by store",
                    "description": "Retrieve total and average sales amounts for a specific store.",
                    "parameters": [
                        {
                            "name": "key_store",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Total and average sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "total_sales": {
                                                "type": "string",
                                                "example": "$1,234.56"
                                            },
                                            "average_sales": {
                                                "type": "string",
                                                "example": "$123.45"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales data found for the given store."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/product/total_avg/": {
                "get": {
                    "summary": "Get total and average sales by product",
                    "description": "Retrieve total and average sales amounts for a spec product.",
                    "parameters": [
                        {
                            "name": "key_product",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Total and average sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "total_sales": {
                                                "type": "string",
                                                "example": "$1,234.56"
                                            },
                                            "average_sales": {
                                                "type": "string",
                                                "example": "$123.45"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales data found for the given product."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/employee/total_avg/": {
                "get": {
                    "summary": "Get total and average sales by employee",
                    "description": "Retrieve total and average sales amounts for a spec employee.",
                    "parameters": [
                        {
                            "name": "key_employee",
                            "in": "query",
                            "required": True,
                            "schema": {
                                "type": "string"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Total and average sales data retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "total_sales": {
                                                "type": "string",
                                                "example": "$1,234.56"
                                            },
                                            "average_sales": {
                                                "type": "string",
                                                "example": "$123.45"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No sales data found for the given employee."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/sales/first_record/": {
                "get": {
                    "summary": "Get the first record",
                    "description": "Retrieve the first record in the dataset.",
                    "responses": {
                        "200": {
                            "description": "First record retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "additionalProperties": True
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "No data available."
                        }
                    },
                    "security": [
                        {
                            "BearerAuth": []
                        }
                    ]
                }
            },
            "/auth/login": {
                "post": {
                    "summary": "User login",
                    "description": "Authenticate a user and return a JWT token.",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "email": {
                                            "type": "string",
                                            "format": "email",
                                            "example": "test@mail.com"
                                        },
                                        "password": {
                                            "type": "string",
                                            "example": "Test123"
                                        }
                                    },
                                    "required": ["email", "password"]
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Token retrieved successfully",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "token": {
                                                "type": "string",
                                                "example": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Invalid credentials or other error"
                        }
                    }
                }
            }
        },
        "components": {
            "securitySchemes": {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [
            {
                "BearerAuth": []
            }
        ]
    }
