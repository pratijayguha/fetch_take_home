# <TODO> Add header doc.

# Imports
import os

# PATH variables
PROJECT_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PROJECT_PATH, "data")
PLOTS_PATH = os.path.join(PROJECT_PATH, "plots")

USERS_CSV_PATH = os.path.join(DATA_PATH, "raw", "USER_TAKEHOME.csv")
TRANSACTIONS_CSV_PATH = os.path.join(DATA_PATH, "raw", "TRANSACTION_TAKEHOME.csv")
PRODUCTS_CSV_PATH = os.path.join(DATA_PATH, "raw", "PRODUCTS_TAKEHOME.csv")

USERS_SAMPLE_CSV_PATH = os.path.join(DATA_PATH, "raw", "sample", "users.csv")
TRANSACTIONS_SAMPLE_CSV_PATH = os.path.join(
    DATA_PATH, "raw", "sample", "transactions.csv"
)
PRODUCTS_SAMPLE_CSV_PATH = os.path.join(DATA_PATH, "raw", "sample", "products.csv")

USERS_CLEAN_PARQUET_PATH = os.path.join(DATA_PATH, "clean", "users.parquet")
TRANSACTIONS_CLEAN_PARQUET_PATH = os.path.join(
    DATA_PATH, "clean", "transactions.parquet"
)
PRODUCTS_CLEAN_PARQUET_PATH = os.path.join(DATA_PATH, "clean", "products.parquet")

