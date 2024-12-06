import snowflake.connector
from core.config import settings

def get_connection():
    return snowflake.connector.connect(
        user=settings.snowflake_user,
        password=settings.snowflake_password,
        account=settings.snowflake_account,
        warehouse=settings.snowflake_warehouse,
        database=settings.snowflake_database,
        schema=settings.snowflake_schema,
        insecure_mode=True

    )
