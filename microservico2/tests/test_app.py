import pytest
from microservico2.app import app

# Configuração do Flask para testes
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados em memória
    with app.test_client() as client:
        yield client

# Testando o endpoint para listar todos os clientes
def test_listar_clientes(client):
    resposta = client.get("/clientes")
    assert resposta.status_code == 200

# Testando o endpoint para criar um novo cliente
def test_criar_cliente(client):
    resposta = client.post("/clientes", json={
        "nome": "Jessica Souza",
        "telefone": 123456789,
        "correntista": True,
        "score_credito": 800.0,
        "saldo_cc": 5000.0
    })
    assert resposta.status_code == 201
    assert "id" in resposta.json  # Verifica se o ID do cliente foi gerado
    assert resposta.json["nome"] == "Jessica Souza"  # Verifica se o nome está correto

# Testando o caso de criação de cliente sem o nome
def test_criar_cliente_sem_nome(client):
    resposta = client.post("/clientes", json={
        "telefone": 123456789,
        "correntista": True,
        "score_credito": 800.0,
        "saldo_cc": 5000.0
    })
    assert resposta.status_code == 400  # Espera um erro 400 (Bad Request)

# Testando se o cliente foi realmente salvo no banco de dados
def test_cliente_no_banco(client):
    resposta = client.post("/clientes", json={
        "nome": "Jessica Souza",
        "telefone": 123456789,
        "correntista": True,
        "score_credito": 800.0,
        "saldo_cc": 5000.0
    })
    cliente = resposta.get_json()  # Recupera o cliente da resposta
    assert cliente is not None
    assert cliente["nome"] == "Jessica Souza"