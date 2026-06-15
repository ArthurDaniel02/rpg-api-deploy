# RPG EDUCACIONAL API REST 🚀

Este projeto consiste em uma API REST desenvolvida em **Python** utilizando **Django** e **Django REST Framework (DRF)**, com base nos diagramas de classes produzidos para o projeto RPG educacional, desenvolvido na matéria Engenharia de Software 2.

O foco é a aplicação prática de **Polimorfismo, Inversão de Dependência e Arquitetura em Camadas**, utilizando interfaces baseadas em Classes Abstratas para simular contratos e injeção dinâmica de implementações.

## 🗺️ Rotas REST Implementadas

Abaixo estão as principais rotas desenvolvidas para atender as regras de negócio do RPG Educacional. Todas recebem e retornam dados em formato JSON.

### 1. CONTA
* `POST /api/conta/` - Salvar (Cria uma nova conta).
* `GET /api/conta/` - Consultar Todos.
* `GET /api/conta/<id>/` - Consultar por ID.
* `PUT /api/conta/<id>/` - Alterar conta existente.
* `DELETE /api/conta/<id>/` - Deletar conta.
* `POST /api/conta/login/` - Realizar Login (Valida email e senha).

### 2. PESSOA
* `POST /api/pessoa/` - Salvar (Cria uma nova pessoa).
* `GET /api/pessoa/` - Consultar Todos.
* `GET /api/pessoa/<id>/` - Consultar por ID.
* `PUT /api/pessoa/<id>/` - Alterar pessoa.
* `DELETE /api/pessoa/<id>/` - Deletar pessoa.

### 3. ALUNO
* `POST /api/aluno/` - Salvar (Cria um novo aluno).
* `GET /api/aluno/` - Consultar Todos.
* `GET /api/aluno/<id>/` - Consultar por ID.
* `PUT /api/aluno/<id>/` - Alterar aluno.
* `DELETE /api/aluno/<id>/` - Deletar aluno.
* `POST /api/aluno/comprar/` - Comprar Item (Desconta moedas e associa item ao inventário).
* `GET /api/aluno/<id>/itens/` - Consultar itens comprados e presentes no inventário do aluno.

### 4. PROFESSOR
* `POST /api/professor/` - Salvar (Cria um novo professor).
* `GET /api/professor/` - Consultar Todos.
* `GET /api/professor/<id>/` - Consultar por ID.
* `PUT /api/professor/<id>/` - Alterar professor.
* `DELETE /api/professor/<id>/` - Deletar professor.
* `GET /api/professor/<id>/disciplinas/` - Consultar todas as disciplinas ministradas pelo professor.

### 5. PERSONAGEM
* `POST /api/personagem/` - Salvar (Cria um novo personagem, operando como uma *Factory* para Mago, Guerreiro ou Arqueiro).
* `GET /api/personagem/` - Consultar Todos.
* `GET /api/personagem/<id>/` - Consultar por ID.
* `PUT /api/personagem/<id>/` - Alterar personagem.
* `DELETE /api/personagem/<id>/` - Deletar personagem.

### 6. DISCIPLINA
* `POST /api/disciplina/` - Salvar (Cria uma nova disciplina).
* `GET /api/disciplina/` - Consultar Todos.
* `GET /api/disciplina/<id>/` - Consultar por ID.
* `PUT /api/disciplina/<id>/` - Alterar disciplina.
* `DELETE /api/disciplina/<id>/` - Deletar disciplina.
* `POST /api/disciplina/matricular/` - Matricular Aluno na disciplina.
* `GET /api/disciplina/<id>/alunos/` - Consultar a lista de todos os alunos matriculados na disciplina.

### 7. QUESTS
* `POST /api/quests/` - Salvar (Cria uma nova quest de múltipla escolha com recompensa customizável).
* `GET /api/quests/` - Consultar Todos.
* `GET /api/quests/<id>/` - Consultar por ID.
* `PUT /api/quests/<id>/` - Alterar quest.
* `DELETE /api/quests/<id>/` - Deletar quest.
* `POST /api/quests/responder/` - Responder Quest (Valida a resposta e deposita a recompensa em moedas na conta do aluno).

### 8. ITEM
* `POST /api/item/` - Salvar (Cria um novo item na loja).
* `GET /api/item/` - Consultar Todos.
* `GET /api/item/<id>/` - Consultar por ID.
* `PUT /api/item/<id>/` - Alterar item.
* `DELETE /api/item/<id>/` - Deletar item.

## Telas da Aplicação (Testes Funcionais)

Como este projeto é estritamente uma API REST (Back-end), as "telas" da aplicação consistem nas interfaces de documentação e administração.

### 1. Swagger UI (Documentação Interativa)
A interface do Swagger permite visualizar e testar todas as rotas listadas acima diretamente pelo navegador.
* **Link para teste:** `http://localhost:8000/api/docs/`

![Tela Exemplo 1 do Swagger]([tela1.png])  
![Tela Exemplo 2 do Swagger]([tela2.png])  
*(Exemplo de teste funcional interativo via Swagger)*

### 2. Painel Administrativo (Django Admin)
Interface gráfica gerada para gerenciamento direto do banco de dados (MySQL), permitindo a inserção e verificação visual dos dados.
* **Link para teste:** `http://localhost:8000/admin/`
* **Credenciais de Teste:** Usuário: `admin` | Senha: `adminsenha`

![Tela do Django Admin]([tela3.png])  
*(Visão geral e gerenciamento dos modelos do RPG no banco de dados)*

## 📚 Objetivo

Demonstrar a aplicação de padrões de projeto e princípios de POO em um framework (Django), garantindo:

* **Desacoplamento:** Camadas de Controller e DAO isoladas.
* **Polimorfismo:** Troca dinâmica de implementações via `config.py`.
* **Contratos:** Uso de classes base para definir comportamentos obrigatórios.

## 🧠 Estratégia Polimórfica

O projeto organiza a lógica de persistência e controle em três partes:

### 1. Controllers
Baseados em interfaces (`api/interfaces/controllers/`), definem métodos CRUD (`salvar`, `alterar`, `deletar`, `consultar`, `consultarbyId`).
* **Exemplo:** `ContaControllerImpl` implementa a lógica, delegando a persistência ao DAO injetado.

### 2. DAO (Data Access Object)
Baseados em interfaces (`api/interfaces/daos/`), abstraem a comunicação com o banco de dados.
* **Implementação:** `NomeEntidadeDAO_Mysql` realiza a persistência via **Django ORM** e **MySQL**.

### 3. Injeção de Dependência via `config.py`
O arquivo `api/config.py` atua como o orquestrador. Ele define quais classes concretas serão instanciadas em tempo de execução:

```python
# Exemplo de configuração de injeção
CONFIG = {
    'IContaDAO': 'api.persistence.ContaDAO_Mysql.ContaDAOMysql',
    'IContaController': 'api.controllers.ContaController.ContaControllerImpl',
}

Isso permite alterar o comportamento da aplicação (trocar o DAO de MySQL para outro, por exemplo) sem alterar o código do Controller ou da View.

## ⚙️ Tecnologias Utilizadas

* **Python 3.14**
* **Django 6.0.6**
* **Django REST Framework**
* **MySQL** (Banco de dados local via MySQL Workbench)
* **drf-spectacular** (Swagger/OpenAPI)

## 🏗️ Fluxo da Aplicação

1. A **View** recebe a requisição HTTP.
2. A View chama a função `inject()` de `config.py`.
3. O `config.py` instancia dinamicamente o **Controller** e seu respectivo **DAO**.
4. O Controller processa a regra de negócio e retorna um dicionário padrão para a View, que responde com um `JsonResponse`.

## 🛠️ Execução

```bash
# 1. Clone o repositório
git clone https://github.com/ArthurDaniel02/RPGEDUCACIONAL2.0/
cd rpg

# 2. Ative o ambiente virtual
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o banco local (MySQL Workbench)
# Crie o banco: 
CREATE DATABASE rpg_educacional_db;
USE rpg_educacional_db;

# 5. Aplique as migrações e rode o servidor
python manage.py migrate
python manage.py runserver

```

**Servidor:** `http://localhost:8000/api/`
**Documentação (Swagger):** `http://localhost:8000/api/docs/`

## 🎯 Conclusão

O projeto prova que, mesmo utilizando frameworks opinativos como o Django, é possível aplicar conceitos avançados de engenharia de software para garantir um código modular, extensível e testável, separando a lógica de negócio da infraestrutura de persistência.

## 👨‍💻 Grupo

* Arthur Daniel Ribeiro Pereira Dantas Lourenço
* Danilo Moraes Borges Piquiá
* Matheus Oliveira Gouveia Campos

---

*Nota: Este projeto utiliza um banco de dados MySQL rodando localmente (localhost:3306).*