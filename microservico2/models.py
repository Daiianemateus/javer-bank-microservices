from .database import db

class Cliente(db.Model): # Define o modelo Cliente para o banco de dados
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # ID único e autoincrementável
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.BigInteger, nullable=False)
    correntista = db.Column(db.Boolean, default=True)
    score_credito = db.Column(db.Float, nullable=False)
    saldo_cc = db.Column(db.Float, nullable=False)

    def to_json(self): # Converte o objeto Cliente para um formato JSON
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "correntista": self.correntista,
            "score_credito": self.score_credito,
            "saldo_cc": self.saldo_cc
        }
