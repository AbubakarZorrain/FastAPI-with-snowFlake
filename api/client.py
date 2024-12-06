from fastapi import APIRouter, Depends, HTTPException, status
from core.database import get_connection
from services.client_service import ClientService
from repositories.client_repository import ClientRepository
import snowflake.connector
 
client_router = APIRouter()

def get_client_service(connection: snowflake.connector.connection.SnowflakeConnection = Depends(get_connection)):
    client_repository = ClientRepository(connection)
    return ClientService(client_repository)

@client_router.get("/")
async def get_all_clients(service: ClientService = Depends(get_client_service)):
    return await service.get_all_clients()

@client_router.get("/{client_id}")
async def get_client(client_id: int, service: ClientService = Depends(get_client_service)):
    client = await service.get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@client_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_client(client_data: dict, service: ClientService = Depends(get_client_service)):
    return await service.create_client(
        name=client_data["name"],
        email=client_data["email"],
        phone=client_data.get("phone")
    )

@client_router.put("/{client_id}")
async def update_client(client_id: int, client_data: dict, service: ClientService = Depends(get_client_service)):
    updated_client = await service.update_client(client_id, client_data)
    if not updated_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return updated_client

@client_router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: int, service: ClientService = Depends(get_client_service)):
    deleted_client = await service.delete_client(client_id)
    if not deleted_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}
