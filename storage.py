import json
from datetime import datetime

ARQUIVO = "dados.json"

def salvar_dados(entrada: dict, resultado: float):
    """Salva entrada + resultado em um arquivo JSON com timestamp"""
    try:
        with open(ARQUIVO, "r") as f:
            historico = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        historico = []

    historico.append({
        "timestamp": datetime.utcnow().isoformat(),
        "entrada": entrada,
        "resultado": resultado
    })

    with open(ARQUIVO, "w") as f:
        json.dump(historico, f, indent=2)
        
def ler_historico():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []