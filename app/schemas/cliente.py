from datetime import datetime
from pydantic import BaseModel, Field


class ClienteCreate(BaseModel):
    nome: str = Field(max_length=100)
    email: str = Field(max_length=255)
    telefone: str = Field(max_length=20)


class ClienteUpdate(BaseModel):
    nome: str = Field(max_length=100)
    email: str = Field(max_length=255)
    telefone: str = Field(max_length=20)


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    data_criacao: datetime
    ativo: bool
