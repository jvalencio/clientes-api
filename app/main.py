from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API de Clientes online"}
