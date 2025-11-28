def criar_produto(id_produto: int, nome: str, quantidade: float, preco: float) -> dict:
    return {
        "id": int(id_produto),          # Converte o ID para inteiro
        "nome": str(nome).strip(),      # Garante string e remove espaços extras nas extremidades
        "quantidade": float(quantidade),# Converte a quantidade para float
        "preco": float(preco)           # Converte o preço para float
    }
