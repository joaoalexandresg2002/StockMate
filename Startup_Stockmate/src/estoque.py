import csv
import os
from typing import Dict, List, Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")  # Caminho da pasta /data
CSV_PATH = os.path.join(DATA_DIR, "produtos.csv")                 # Caminho do arquivo CSV

estoque: List[Dict] = []  # Lista que guarda os produtos como dicionários

def _garantir_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)  # Cria a pasta data caso não exista

def salvar_csv(path: str = CSV_PATH) -> None:
    _garantir_data_dir()  # Garante que o diretório exista
    campos = ("id", "nome", "quantidade", "preco")  # Cabeçalhos do CSV

    with open(path, "w", newline="", encoding="utf-8") as f:  # Abre o CSV para escrita
        writer = csv.DictWriter(f, fieldnames=campos)  # Cria escritor de dicionário
        writer.writeheader()  # Escreve cabeçalhos
        writer.writerows(estoque)  # Salva todos os produtos

def carregar_csv(path: str = CSV_PATH) -> None:
    if not os.path.exists(path):  # Se não existe, não carrega nada
        return

    with open(path, "r", newline="", encoding="utf-8") as f:  # Abre o CSV
        reader = csv.DictReader(f)  # Lê cada linha como dicionário
        estoque.clear()  # Limpa o estoque atual
        for row in reader:  # Percorre cada linha
            try:
                estoque.append({
                    "id": int(row["id"]),                   # Converte id
                    "nome": row["nome"],                   # Nome
                    "quantidade": int(row["quantidade"]),   # Quantidade
                    "preco": float(row["preco"])            # Preço
                })
            except (KeyError, ValueError, TypeError):
                continue  # Ignora linhas com erros

try:
    carregar_csv()  # Tenta carregar o CSV ao iniciar
except Exception:
    pass  # Ignora qualquer erro no carregamento inicial

def _buscar_indice_por_id(id_produto: int) -> Optional[int]:
    for i, p in enumerate(estoque):  # Procura produto pelo ID
        if p["id"] == id_produto:
            return i  # Retorna o índice encontrado
    return None  # Se não achar, retorna None

def adicionar_produto(produto: Dict) -> bool:
    if _buscar_indice_por_id(produto["id"]) is not None:  # Checa se ID já existe
        return False

    estoque.append({  # Adiciona o produto ao estoque
        "id": int(produto["id"]),
        "nome": str(produto["nome"]),
        "quantidade": int(produto["quantidade"]),
        "preco": float(produto["preco"])
    })
    return True

def remover_produto(id_produto: int) -> bool:
    idx = _buscar_indice_por_id(id_produto)  # Busca índice
    if idx is None:
        return False
    estoque.pop(idx)  # Remove o produto
    return True

def atualizar_quantidade(id_produto: int, nova_quantidade: int) -> bool:
    idx = _buscar_indice_por_id(id_produto)  # Busca produto
    if idx is None:
        return False
    estoque[idx]["quantidade"] = int(nova_quantidade)  # Atualiza quantidade
    return True

def ajustar_estoque(id_produto: int, delta: int) -> bool:
    idx = _buscar_indice_por_id(id_produto)  # Busca produto
    if idx is None:
        return False

    nova = estoque[idx]["quantidade"] + int(delta)  # Soma quantidade
    estoque[idx]["quantidade"] = max(nova, 0)       # Evita valores negativos
    return True

def listar_produtos() -> List[Dict]:
    return [p.copy() for p in estoque]  # Retorna cópias dos produtos

def buscar_produto(id_produto: int) -> Optional[Dict]:
    idx = _buscar_indice_por_id(id_produto)  # Busca índice
    return None if idx is None else estoque[idx].copy()  # Retorna cópia ou None

def produto_abaixo_minimo(limite: int = 5) -> List[Dict]:
    return [p.copy() for p in estoque if p["quantidade"] <= limite]  # Filtra produtos críticos
