"""Data model for a sales transaction.

Tasks (see chapter Task 2):
  1. Define a Transaction dataclass with the fields listed below.
  2. Use __post_init__ to enforce: price >= 0 and product_name non-empty.

The pipeline converts cleaned dicts into Transaction instances at the
boundary, so the dataclass is the schema-of-record for everything that
gets written to the output CSV.
"""
from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_id: int
    product_name: str
    category: str
    price: float
    quantity: int
    customer_email: str
    date: str
    revenue: float = 0.0
    vat: float = 0.0

    def __post_init__(self):
      self.price = float(self.price)
      if self.price < 0:
         raise ValueError(f"Price should not be negtive: {self.price}")
      if not self.product_name.strip():
         raise ValueError("Product name should not be empty or whitespace-only")
  
