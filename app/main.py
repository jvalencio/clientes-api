from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteResponse


app = FastAPI()


@app.get("/")
def root():
    return {"message": "API de Clientes online"}


@app.get("/clientes", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes


@app.get("/clientes/{id}", response_model=ClienteResponse)
def buscar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente


@app.put("/cliente/{id}", response_model=ClienteResponse)
def atualizar_cliente(id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id == id).first()

    if cliente_db is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    cliente_db.nome = cliente.nome
    cliente_db.email = cliente.email
    cliente_db.telefone = cliente.telefone

    db.commit()
    db.refresh(cliente_db)

    return cliente_db


@app.delete("/clientes/{id}")
def deletar_cliente(id: int, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id == id).first()

    if cliente_db is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )
    
    db.delete(cliente_db)
    db.commit()

    return {"message": "Cliente deletado com sucesso"}


@app.post("/clientes", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    novo_cliente = Cliente(
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente
