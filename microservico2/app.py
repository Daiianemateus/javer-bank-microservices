from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .database import db
from .models import Cliente

app = Flask(__name__) # Inicializa a aplicação Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes.db"  # Usando SQLite local
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Desativa notificações de modificações desnecessárias

db.init_app(app) # Inicializa a conexão com o banco de dados

# Criar o banco de dados
with app.app_context():
    db.create_all()

# Criar um novo cliente (Create)
@app.route("/clientes", methods=["POST"])
def criar_cliente():
    dados = request.get_json()

    # Verifique se o campo 'nome' está presente no corpo da requisição
    if "nome" not in dados:
        return jsonify({"erro": "O campo 'nome' é obrigatório!"}), 400

    try:
        # Tente criar o cliente, se os dados estiverem corretos
        novo_cliente = Cliente(
            nome=dados["nome"],
            telefone=dados["telefone"],
            correntista=dados["correntista"],
            score_credito=dados["score_credito"],
            saldo_cc=dados["saldo_cc"]
        )
        db.session.add(novo_cliente)
        db.session.commit()

        # Retorne os dados do cliente criado, incluindo o 'id'
        return jsonify({
            "id": novo_cliente.id,
            "nome": novo_cliente.nome,
            "telefone": novo_cliente.telefone,
            "correntista": novo_cliente.correntista,
            "score_credito": novo_cliente.score_credito,
            "saldo_cc": novo_cliente.saldo_cc
        }), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
    
# Obter todos os clientes (Read)
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.all() # Consulta todos os clientes
    return jsonify([c.to_json() for c in clientes]) # Retorna a lista de clientes

# Obter um cliente por ID (Read)
@app.route("/clientes/<int:id>", methods=["GET"])
def obter_cliente(id):
    cliente = Cliente.query.get(id) # Busca um cliente pelo ID
    if cliente:
        return jsonify(cliente.to_json())  # Retorna os dados do cliente
    return jsonify({"mensagem": "Cliente não encontrado"}), 404 # Retorna erro se o cliente não existir

# Atualizar um cliente (Update)
@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    cliente = Cliente.query.get(id)# Busca um cliente pelo ID
    if not cliente:
        return jsonify({"mensagem": "Cliente não encontrado"}), 404  # Retorna erro se não existir

    dados = request.json # Obtém os dados enviados para atualização
    cliente.nome = dados.get("nome", cliente.nome)
    cliente.telefone = dados.get("telefone", cliente.telefone)
    cliente.correntista = dados.get("correntista", cliente.correntista)
    cliente.score_credito = dados.get("score_credito", cliente.score_credito)
    cliente.saldo_cc = dados.get("saldo_cc", cliente.saldo_cc)

    db.session.commit()  # Confirma a atualização
    return jsonify(cliente.to_json()) # Retorna os dados atualizados

# Deletar um cliente (Delete)
@app.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    cliente = Cliente.query.get(id) # Busca um cliente pelo ID
    if not cliente:
        return jsonify({"mensagem": "Cliente não encontrado"}), 404 # Retorna erro se não existir

    db.session.delete(cliente) # Remove o cliente do banco de dados
    db.session.commit() # Confirma a exclusão
    return jsonify({"mensagem": "Cliente deletado com sucesso"}), 200 # Retorna mensagem de sucesso

if __name__ == "__main__":
    app.run(debug=True) # Inicia o servidor Flask em modo debug
