from fastapi import FastAPI
from models import CapacidadeRequest
from logic import calcular_capacidade
from storage import salvar_dados, ler_historico

app = FastAPI()

@app.post("/calcular")
def calcular(request: CapacidadeRequest):
    resultado = calcular_capacidade(
        request.disponibilidade_por_pessoa,
        request.fator_capacidade
    )
    salvar_dados(request.model_dump(), resultado)  # ⬅️ salva os dados
    return {"capacidade_produtiva": resultado}

@app.get("/historico")
def historico():
    return ler_historico()