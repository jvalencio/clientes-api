# API CRUD de Clientes

API REST desenvolvida com **Python e FastAPI** para gerenciamento de clientes.

Este projeto foi desenvolvido com o objetivo de colocar em prática conceitos de desenvolvimento de APIs, integração com banco de dados, validação de dados, ORM e gerenciamento de migrations.

## 🚀 Tecnologias

* **Python** — linguagem utilizada no desenvolvimento
* **FastAPI** — framework para construção da API
* **Pydantic** — validação e serialização dos dados
* **SQLAlchemy** — ORM para interação com o banco de dados
* **PostgreSQL** — banco de dados relacional
* **Alembic** — gerenciamento de migrations
* **Uvicorn** — servidor utilizado para executar a aplicação

## 📌 Funcionalidades

A API possui as principais operações de um CRUD:

| Método   | Endpoint         | Descrição             |
| -------- | ---------------- | --------------------- |
| `POST`   | `/clientes`      | Criar um cliente      |
| `GET`    | `/clientes`      | Listar clientes       |
| `GET`    | `/clientes/{id}` | Buscar cliente por ID |
| `PUT`    | `/clientes/{id}` | Atualizar um cliente  |
| `DELETE` | `/clientes/{id}` | Deletar um cliente    |

### Validações e tratamento de erros

A API também possui:

* validação dos campos obrigatórios;
* limite de caracteres para os campos;
* validação do formato dos emails;
* prevenção de emails duplicados;
* tratamento de clientes não encontrados;
* respostas HTTP apropriadas para diferentes situações;
* formatação da data de criação dos clientes nas respostas.

## 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** como banco de dados e **SQLAlchemy** como ORM.

A estrutura do banco é gerenciada pelo **Alembic**, permitindo controlar alterações através de migrations.

### Estrutura principal da tabela `clientes`

* `id`
* `nome`
* `email`
* `telefone`
* `data_criacao`
* `ativo`

## 📂 Estrutura do Projeto

```text
clientes-api/
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── cliente.py
│   ├── schemas/
│   │   └── cliente.py
│   ├── database.py
│   └── main.py
├── .gitignore
├── alembic.ini
├── README.md
└── requirements.txt
```

## ▶️ Executando o projeto

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/jvalencio/clientes-api
cd clientes-api
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a variável `DATABASE_URL` no arquivo `.env`:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/clientes_db
```

Execute as migrations:

```bash
alembic upgrade head
```

Inicie a aplicação:

```bash
uvicorn app.main:app --reload
```

A documentação interativa da API estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Objetivo do projeto

Este projeto faz parte do meu processo de aprendizado em desenvolvimento backend e foi desenvolvido com foco em compreender, na prática, o funcionamento de uma API REST, desde o recebimento e validação dos dados até sua persistência em um banco de dados relacional.

O projeto também foi utilizado para aprofundar conhecimentos em **Git, GitHub, SQLAlchemy, PostgreSQL e Alembic**.
