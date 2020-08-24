"""General purpose project utilities."""
import dotenv
import os
import pathlib


# Load project environment variables.
dotenv.load_dotenv()


# Voxco database URL.
USERNAME = os.getenv("USERNAME")
PW = os.getenv("PW")
DSN = os.getenv("DSN")
URL = f"mssql+pyodbc://{USERNAME}:{PW}@{DSN}"


# Project ID.
PROJECT_ID = os.getenv("PROJECT_ID")


# The project root directory.
ROOT = pathlib.Path(__file__, "..", "..").resolve()


# Paths to project directories.
PATHS = {
    "root": ROOT,
    "data": ROOT / "data",
    "raw": ROOT / "data" / "raw",
    "processed": ROOT / "data" / "processed",
    "reports": ROOT / "reports",
    "css": ROOT / "reports" / "css",
    "images": ROOT / "reports" / "images",
    "templates": ROOT / "reports" / "templates",
}
