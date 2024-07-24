import glob
from contextlib import asynccontextmanager

from fastapi import APIRouter, HTTPException, FastAPI
from app.routers.utils import calculate_totals_and_averages, validate_dates
import pandas as pd
from app.datamart import df

router = APIRouter()


file_path = 'app/data/'
all_files = glob.glob(file_path + "data_chunk*.snappy.parquet")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application. Used for setup and teardown tasks.
    """
    global df
    yield


def filter_dataframe(key: str, start_date: str, end_date: str, key_column: str) -> pd.DataFrame:
    """
    Filters the dataframe based on a specific key, start date, end date, and key column.

    Args:
        key (str): The value to filter by.
        start_date (str): The start date for filtering.
        end_date (str): The end date for filtering.
        key_column (str): The column to filter by.

    Returns:
        pd.DataFrame: The filtered dataframe.
    """
    start_date_dt, end_date_dt = validate_dates(start_date, end_date)
    df['KeyDate'] = pd.to_datetime(df['KeyDate']).dt.date
    return df[(df[key_column] == key) &
              (df['KeyDate'] >= start_date_dt) &
              (df['KeyDate'] <= end_date_dt)]


@router.get("/employee/")
def get_sales_by_employee(key_employee: str, start_date: str, end_date: str):
    """
    Retrieves sales data for a specific employee within a given date range.

    Args:
        key_employee (str): The employee's key to filter by.
        start_date (str): The start date for filtering.
        end_date (str): The end date for filtering.

    Returns:
        List[dict]: A list of dictionaries representing the sales data.
    """
    filtered_df = filter_dataframe(key_employee, start_date, end_date, 'KeyEmployee')
    if len(filtered_df) == 0:
        raise HTTPException(status_code=404, detail="No sales data found for the given employee and date range.")
    return filtered_df.to_dict(orient='records')


@router.get("/product/")
def get_sales_by_product(key_product: str, start_date: str, end_date: str):
    """
    Retrieves sales data for a specific product within a given date range.

    Args:
        key_product (str): The product's key to filter by.
        start_date (str): The start date for filtering.
        end_date (str): The end date for filtering.

    Returns:
        List[dict]: A list of dictionaries representing the sales data.
    """
    filtered_df = filter_dataframe(key_product, start_date, end_date, 'KeyProduct')
    if len(filtered_df) == 0:
        raise HTTPException(status_code=404, detail="No sales data found for the given product and date range.")
    return filtered_df.to_dict(orient='records')


@router.get("/store/")
def get_sales_by_store(key_store: str, start_date: str, end_date: str):
    """
    Retrieves sales data for a specific store within a given date range.

    Args:
        key_store (str): The store's key to filter by.
        start_date (str): The start date for filtering.
        end_date (str): The end date for filtering.

    Returns:
        List[dict]: A list of dictionaries representing the sales data.
    """
    filtered_df = filter_dataframe(key_store, start_date, end_date, 'KeyStore')
    if len(filtered_df) == 0:
        raise HTTPException(status_code=404, detail="No sales data found for the given store and date range.")
    return filtered_df.to_dict(orient='records')


@router.get("/store/total_avg/")
def get_total_avg_sales_by_store(key_store: str):
    """
    Retrieves total and average sales data for a specific store.

    Args:
        key_store (str): The store's key to filter by.

    Returns:
        dict: A dictionary containing total and average sales data.
    """
    filtered_df = df[df['KeyStore'] == key_store]
    return calculate_totals_and_averages(filtered_df)


@router.get("/product/total_avg/")
def get_total_avg_sales_by_product(key_product: str):
    """
    Retrieves total and average sales data for a specific product.

    Args:
        key_product (str): The product's key to filter by.

    Returns:
        dict: A dictionary containing total and average sales data.
    """
    filtered_df = df[df['KeyProduct'] == key_product]
    return calculate_totals_and_averages(filtered_df)


@router.get("/employee/total_avg/")
def get_total_avg_sales_by_employee(key_employee: str):
    """
    Retrieves total and average sales data for a specific employee.

    Args:
        key_employee (str): The employee's key to filter by.

    Returns:
        dict: A dictionary containing total and average sales data.
    """
    filtered_df = df[df['KeyEmployee'] == key_employee]
    return calculate_totals_and_averages(filtered_df)


@router.get("/first_record/")
def get_first_record():
    """
    Retrieves the first record from the dataframe.

    Returns:
        dict: A dictionary representing the first record.

    Raises:
        HTTPException: If no data is available, raises a 404 error.
    """
    if len(df.index) == 0:
        raise HTTPException(status_code=404, detail="No data available.")
    first_record = df.iloc[0].to_dict()
    return first_record
