from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_serializer


class ClienteCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(max_length=255)
    telefone: str = Field(min_length=1, max_length=20)


class ClienteUpdate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(max_length=255)
    telefone: str = Field(min_length=1, max_length=20)


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    data_criacao: datetime
    ativo: bool

    @field_serializer("data_criacao")
    def formatar_data_criacao(self, data: datetime) -> str:
        return data.strftime("%d/%m/%Y %H:%M")
