def calcular_capacidade(disponibilidade_por_pessoa, fator_capacidade):
    """
    Exemplo:
    disponibilidade_por_pessoa = [40, 38, 42]
    fator_capacidade = 0.75  # 75%
    """
    capacidade_total = sum(disponibilidade_por_pessoa)
    capacidade_ajustada = capacidade_total * fator_capacidade
    return round(capacidade_ajustada, 2)