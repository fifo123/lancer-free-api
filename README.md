# Lancer Free API

API para gerenciamento de projetos de freelancer.

## Funcionalidades

- **Projetos**: CRUD completo para projetos, permitindo criar, listar, atualizar e deletar projetos.
- **Tarefas**: Gerenciamento de tarefas associadas a cada projeto.
- **Templates**: Criação e gerenciamento de templates de projetos para agilizar a criação de novos projetos.
- **Dashboard**: Visualização de dados e estatísticas sobre os projetos, como somatório de valores por status.

## Tecnologias

- **[Flask](https://flask.palletsprojects.com/)**: Microframework web para Python.
- **[Flask-OpenAPI3](https://github.com/nblask/flask-openapi3)**: Geração de documentação OpenAPI 3.0 para Flask.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM para interação com o banco de dados.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Validação de dados.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: Lida com Cross-Origin Resource Sharing (CORS).

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.12 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd back
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode o projeto:**
   ```bash
   python app.py
   ```

O servidor estará rodando em `http://0.0.0.0:8000`. A documentação da API (Swagger UI) estará disponível em `http://0.0.0.0:8000/swagger`.

## Estrutura do Projeto

```
/
├── .gitignore
├── .python-version
├── app.py              # Ponto de entrada da aplicação Flask
├── database.py         # Configuração da conexão com o banco de dados
├── README.md
├── requirements.txt    # Lista de dependências do projeto
├── database/           # Arquivos do banco de dados (ex: .db)
├── models/             # Definições dos modelos SQLAlchemy (tabelas do banco)
├── routes/             # Definição das rotas/endpoints da API
├── schemas/            # Esquemas Pydantic para validação de dados
└── services/           # Lógica de negócio da aplicação
```
