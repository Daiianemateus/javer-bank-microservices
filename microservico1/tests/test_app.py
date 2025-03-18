import pytest
from unittest.mock import patch
from microservico1.app import app  # Ajuste o import de acordo com a estrutura do seu projeto

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_listar_clientes(client):
    with patch('requests.get') as mock_get:
        # Simula a resposta do microserviço 2
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "nome": "Jessica Souza"}]
        
        # Faz a requisição para a rota
        resposta = client.get("/clientes")
        
        # Verifica o código de status
        assert resposta.status_code == 200
        
        # Verifica se a resposta contém dados simulados
        assert len(resposta.json) > 0
        assert resposta.json[0]["nome"] == "Jessica Souza"

def test_calcular_score(client):
    with patch('requests.get') as mock_get:
        # Simula a resposta do microserviço 2
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "nome": "Jessica Souza", "score_credito": 750.0}
        
        # Faz a requisição para a rota de calcular score
        resposta = client.get("/clientes/1/score")
        
        # Verifica se o código de status é 200
        assert resposta.status_code == 200
        
        # Verifica se o score do cliente está correto
        assert resposta.json['score'] == 750.0
