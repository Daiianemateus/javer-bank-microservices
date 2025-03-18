import requests

BASE_URL = "http://localhost:5000"  # Endereço da segunda aplicação

def obter_cliente(id):
    """Busca um cliente na segunda aplicação pelo ID."""
    response = requests.get(f"{BASE_URL}/clientes/{id}")
    if response.status_code == 200:
        return response.json()
    return None
