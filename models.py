from pydantic import BaseModel
from typing import List

class CapacidadeRequest(BaseModel):
    disponibilidade_por_pessoa: List[float]
    fator_capacidade: float  # ex: 0.75 para 75%