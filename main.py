from fastapi import FastAPI, HTTPException
from api.client import client_router
from core.database import get_connection

app = FastAPI()

# Include Routers
app.include_router(client_router, prefix="/clients", tags=["Clients"])
connection = None

@app.on_event("startup")
def startup_event():
    global connection
    try:
        # Establish the connection to Snowflake when the app starts
        connection = get_connection()
        print("Connected to Snowflake database successfully!")
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        raise HTTPException(status_code=500, detail="Failed to connect to Snowflake DB")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Snowflake Client API"}
