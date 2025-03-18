# javer-bank-microservices - Conectando Microserviços na Nuvem

## Visão Geral
Este projeto implementa dois microserviços interconectados para o **cadastro de clientes** e **cálculo de score de crédito**.  
O **Microserviço 1** realiza operações CRUD de clientes e calcula o score de crédito com base no saldo da conta corrente do cliente, fazendo requisições ao **Microserviço 2**, que armazena os dados dos clientes em um banco de dados utilizando **SQLAlchemy**.

## Tecnologias Utilizadas:
- Python 3.x
- Flask (Framework para criar APIs)
- SQLAlchemy (ORM para gerenciamento do banco de dados)
- SQLite (Banco de dados local)
- Requests (Para comunicação entre os microserviços)

### Como executar
### Passo 1: Clonar o Repositório 
Primeiro, faça o clone do repositório para sua máquina local:

bash
Copy
git clone <URL do repositório>
cd javer-bank-microservices

### Passo 2: Criar o Ambiente Virtual
Crie um ambiente virtual Python para isolar as dependências do projeto:
```bash
python -m venv venv
```

Ative o ambiente virtual:

- Para sistemas Unix (Linux/Mac):
  ```bash
  source venv/bin/activate
  ```

- Para Windows:
  ```bash
  venv\Scripts\activate
  ```
### Passo 3: Instalar as Dependências
Instale as dependências necessárias para o projeto:
```bash
pip install -r requirements.txt

### Passo 3: Instalar as Dependências
Instale as dependências necessárias para o projeto:
```bash
pip install -r requirements.txt
```

### Passo 4: Executar os Microserviços
1. **Inicie o Microserviço 2**, que será responsável pelo armazenamento dos clientes no banco de dados:
   ```bash
   cd microservico2
   python app.py
   ```
   O Microserviço 2 ficará acessível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

2. **Inicie o Microserviço 1**, que realizará as requisições para o Microserviço 2 e calculará o score de crédito:
   ```bash
   cd ../microservico1
   python app.py
   ```
   O Microserviço 1 ficará acessível em: [http://127.0.0.1:5001](http://127.0.0.1:5001)

## Como Testar

### Testando o Microserviço 2
O Microserviço 2 oferece um endpoint para cadastro de clientes via POST.

- **Método:** POST
- **URL:** `http://127.0.0.1:5000/clientes`
- **Body:**
  ```json
  {
    "nome": "João Silva",
    "telefone": 123456789,
    "correntista": true,
    "score_credito": 0,
    "saldo_cc": 1000
  }
  ```
Após enviar a requisição, o Microserviço 2 retornará um status de sucesso com os dados do cliente cadastrado.

### Testando o Microserviço 1
O Microserviço 1 oferece dois principais endpoints:

1. **Cadastro de Cliente:** Realiza uma requisição para o Microserviço 2 e cadastra o cliente.
   - **Método:** POST
   - **URL:** `http://127.0.0.1:5001/clientes`
   - **Body:**
     ```json
     {
       "nome": "Maria Oliveira",
       "telefone": 987654321,
       "correntista": false,
       "score_credito": 0,
       "saldo_cc": 2000
     }
     ```

2. **Calcular Score de Crédito:** Retorna o score de crédito calculado.
   - **Método:** GET
   - **URL:** `http://127.0.0.1:5001/clientes/1/score`
   - **Resposta esperada:**
     ```json
     {
       "id": 1,
       "nome": "João Silva",
       "score_credito_calculado": 100.0
     }
     ```

## Detalhes Técnicos

### Estrutura de Diretórios
```
javer-bank-microservices/
├── microservico1/
│   ├── app.py            # Código do Microserviço 1 (CRUD de clientes e cálculo de score)
│   ├── requirements.txt  # Dependências do Microserviço 1
├── microservico2/
│   ├── app.py            # Código do Microserviço 2 (Cadastro de clientes)
│   ├── requirements.txt  # Dependências do Microserviço 2
├── README.md             # Este arquivo de documentação
```

### Configurações de Ambiente
- O Microserviço 2 usa o banco de dados **SQLite**, que armazena dados localmente.
- Certifique-se de que as URLs dos microserviços estejam corretas. No Microserviço 1, o endpoint do Microserviço 2 está configurado como `MICROSERVICO_2_URL = "http://127.0.0.1:5000"`.

## Considerações Finais
- Para garantir que os microserviços funcionem corretamente, você deve ter o **Python** instalado em sua máquina.
- Teste os endpoints usando ferramentas como **Insomnia** ou **Postman**.
- Os microserviços estão configurados para rodar localmente nas portas **5000** (Microserviço 2) e **5001** (Microserviço 1).
