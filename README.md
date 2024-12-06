# FastAPI Application Setup and Usage Guide

This is a FastAPI application that provides various client-related endpoints, uses SQLAlchemy for database management, and is configured to run with SQLite in an asynchronous environment.

## Prerequisites

Ensure that you have the following installed:

- **Python 3.9+**
- **pip** (Python package manager)

If you don't have them installed, please follow the installation guides below:

- [Install Python](https://www.python.org/downloads/)
- [Install pip](https://pip.pypa.io/en/stable/)

## Installation

###  Create a virtual environment

```bash
python -m venv venv
```
### Install the required dependencies

```bash
pip install -r requirements.txt
```

### Create a .env file for environment variables
```
SNOWFLAKE_USER=<>
SNOWFLAKE_PASSWORD=<>
SNOWFLAKE_ACCOUNT=<>
SNOWFLAKE_DATABASE=<>
SNOWFLAKE_SCHEMA=<>
SNOWFLAKE_WAREHOUSE=<>
```

### Run the Application
```bash
uvicorn main:app --reload
```