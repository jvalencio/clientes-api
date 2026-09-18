# API CRUD de Clientes

Projeto desenvolvido para estudar e aprofundar meus conhecimentos em desenvolvimento de APIs utilizando a linguagem Python.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic

## Funcionalidades

A API permite realizar operações CRUD de clientes:

- `POST /clientes` — criar cliente
- `GET /clientes` — listar clientes
- `GET /clientes/{id}` — buscar cliente por ID
- `PUT /clientes/{id}` — atualizar cliente
- `DELETE /clientes/{id}` — deletar cliente

A API também possui tratamento para clientes não encontrados, retornando `404 Not Found`.

## Banco de Dados

O projeto utiliza PostgreSQL como banco de dados e SQLAlchemy como ORM.

As alterações na estrutura do banco são gerenciadas pelo Alembic através de migrations.