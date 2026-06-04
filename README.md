# 📦 Prática de Stored Procedures (MySQL + Python)

Projeto prático para demonstrar a criação de **Stored Procedures** no banco de dados **MySQL** e sua execução automatizada via **Python**, utilizando o driver oficial `mysql-connector-python`.

---

## 🛠️ Tecnologias
* **Python 3.x**
* **MySQL Database**
* **mysql-connector-python** (`pip install mysql-connector-python python-dotenv`)

---

## 🗂️ Estrutura do Projeto
* `schema.sql` ➔ Estrutura das tabelas e carga inicial de dados.
* `procedures.sql` ➔ Código-fonte das Stored Procedures (`IN`, `OUT`).
* `Estoque.py` ➔ Script Python que conecta ao banco e executa as procedures.
* `.env.example` ➔ Modelo para configuração das credenciais locais.

---

## 🚀 Como Rodar
1. Execute os arquivos `schema.sql` e `procedures.sql` no seu banco MySQL.
2. Instale as dependências: `pip install mysql-connector-python python-dotenv`
3. Crie um arquivo `.env` baseado no `.env.example` com suas credenciais.
4. Rode o script: `python Estoque.py`
