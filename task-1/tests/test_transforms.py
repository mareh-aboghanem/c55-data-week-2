import pytest
import copy

from src.transforms import (
    calculate_revenue,
    clean_fields,
    filter_zero_quantity,
    remove_invalid,
)


def test_remove_invalid_drops_empty_names():
    data = [
        {"product_name": "Laptop", "price": 999.99},
        {"product_name": "", "price": 50.0},
        {"product_name": "  ", "price": 25.0},
    ]
    result = remove_invalid(data)
    assert len(result) == 1
    assert result[0]["product_name"] == "Laptop"


def test_clean_fields_normalizes_names():
    data = [
        {"product_name": "  laptop", "customer_email": "BOB@Company.COM"}
    ]
    result = clean_fields(data)
    
    assert len(result) == 1
    assert result[0]["product_name"] == "Laptop"
    assert result[0]["customer_email"] == "bob@company.com"


def test_calculate_revenue_adds_fields():
    data = [
        {"product_name": "Laptop", "price": 100.0, "quantity": 3}
    ]
    result = calculate_revenue(data)
    
    assert len(result) == 1
    assert result[0]["revenue"] == 300.0
    assert result[0]["vat"] == 63.0


def test_no_mutation():
    original_data = [
        {"product_name": "Laptop", "price": 100.0, "quantity": 1}
    ]
    
    data_to_transform = copy.deepcopy(original_data)
    calculate_revenue(data_to_transform)
    assert data_to_transform == original_data