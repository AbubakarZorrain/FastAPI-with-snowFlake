import snowflake.connector
from models.client import Client

class ClientRepository:
    def __init__(self, connection: snowflake.connector.connection.SnowflakeConnection = None):
        self.connection = connection

    async def get_all(self):
        query = "SELECT * FROM CLIENT;"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    async def get_by_id(self, client_id: int):
        query = f"SELECT * FROM client WHERE id = {client_id};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    async def create(self, client: Client):
        cursor = self.connection.cursor()
        cursor.execute("SELECT client_id_seq.nextval")
        client_id = cursor.fetchone()[0]
        cursor.close()

        query = "INSERT INTO client (id, name, email, phone) VALUES (%s, %s, %s, %s)"
        self.connection.cursor().execute(query, (client_id, client.name, client.email, client.phone))
        return client

    async def update(self, client_id: int, client_data: dict):
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in client_data.items()])
        query = f"UPDATE client SET {set_clause} WHERE id = {client_id};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return client_data

    async def delete(self, client_id: int):
        query = f"DELETE FROM client WHERE id = {client_id};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return {"message": "Client deleted successfully"}
