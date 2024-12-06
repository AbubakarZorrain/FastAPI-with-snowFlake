from repositories.client_repository import ClientRepository
from models.client import Client

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    async def get_all_clients(self):
        return await self.client_repository.get_all()

    async def get_client_by_id(self, client_id: int):
        return await self.client_repository.get_by_id(client_id)

    async def create_client(self, name: str, email: str, phone: str = None):
        new_client = Client(name=name, email=email, phone=phone)
        return await self.client_repository.create(new_client)

    async def update_client(self, client_id: int, client_data: dict):
        return await self.client_repository.update(client_id, client_data)

    async def delete_client(self, client_id: int):
        return await self.client_repository.delete(client_id)
