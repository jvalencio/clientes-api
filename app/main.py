from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate


app = FastAPI()


@app.get("/")
def root():
    return {"message": "API de Clientes online"}


@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes


@app.get("/clientes/{id}")
def buscar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente


@app.put("/cliente/{id}")
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


@app.post("/clientes")
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
