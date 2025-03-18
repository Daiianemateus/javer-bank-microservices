from flask import Flask, request, jsonify
import requests
from unittest.mock import patch

app = Flask(__name__)  # Inicializa a aplicação Flask

# URL do microserviço 2 (onde está o banco de dados)
MICROSERVICO_2_URL = "http://127.0.0.1:5001/clientes"

# Criar um novo cliente (Create)
@app.route("/clientes", methods=["POST"])
def criar_cliente():
    dados = request.json  # Obtém os dados do cliente enviados na requisição
    resposta = requests.post(MICROSERVICO_2_URL, json=dados)  # Envia os dados para o microserviço 2
    return jsonify(resposta.json()), resposta.status_code  # Retorna a resposta recebida

# Obter todos os clientes (Read)
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    resposta = requests.get(MICROSERVICO_2_URL)  # Requisição GET ao microserviço 2 para listar todos os clientes
    if resposta.status_code == 200:
        return jsonify(resposta.json()), 200
    return jsonify({"error": "Não foi possível obter os clientes."}), 500

# Obter um cliente por ID (Read)
@app.route("/clientes/<int:id>", methods=["GET"])
def obter_cliente(id):
    resposta = requests.get(f"{MICROSERVICO_2_URL}/{id}")  # Requisição GET para o microserviço 2 com o ID
    return jsonify(resposta.json()), resposta.status_code  # Retorna a resposta do microserviço 2

# Atualizar um cliente (Update)
@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    dados = request.json  # Obtém os dados enviados para atualização
    resposta = requests.put(f"{MICROSERVICO_2_URL}/{id}", json=dados)  # Envia os dados para o microserviço 2
    return jsonify(resposta.json()), resposta.status_code  # Retorna a resposta

# Deletar um cliente (Delete)
@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    resposta = requests.delete(f"{MICROSERVICO_2_URL}/{id}")  # Envia a requisição DELETE ao microserviço 2
    return jsonify(resposta.json()), resposta.status_code  # Retorna a resposta da exclusão

# Endpoint adicional: calcular score de crédito
@app.route('/clientes/<int:id>/score', methods=['GET'])
def calcular_score(id):
    # Faz uma requisição GET ao microserviço 2 para obter o cliente com o ID
    resposta = requests.get(f"{MICROSERVICO_2_URL}/{id}")
    if resposta.status_code == 200:
        cliente = resposta.json()  # Obtém os dados do cliente
        return jsonify({'score': cliente['score_credito']}), 200  # Retorna o score de crédito
    return jsonify({'message': 'Cliente não encontrado'}), 404  # Caso o cliente não seja encontrado

# Configurações do servidor Flask
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Inicia o servidor Flask na porta 5001, com modo debug ativado

