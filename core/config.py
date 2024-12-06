from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    snowflake_user: str
    snowflake_password: str
    snowflake_account: str
    snowflake_database: str
    snowflake_schema: str
    snowflake_warehouse: str

    class Config:
        env_file = ".env"

settings = Settings()
