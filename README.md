

# ✅ Entregáveis do Projeto

- [x] API funcional com endpoints REST públicos e documentados.
- [x] Autenticação via JWT. (Opicional)
- [x] Documentação dos endpoints via Swagger (`/docs`).
- [ ] Pipeline de ingestão e processamento funcionando.(Opicional)
- [x] Descrição clara da integração com Machine Learning.
- [x] Diagrama da arquitetura adicionado no README.
- [ ] Link do deploy funcionando.



# ✅ Entregáveis do Projeto


username="admin"
password="automate123."



# 🏗️ Plano de Deploy — API de Vitivinicultura + ML

## 🔥 Descrição do Projeto
Desenvolvimento de uma API com **FastAPI** que disponibiliza dados públicos de vitivinicultura da **Embrapa**.  
A API irá alimentar uma pipeline de **Machine Learning**.

---

## 🚀 Arquitetura do Projeto

```plaintext
        +------------------------+
        |      Usuários/API      |
        +-----------+------------+
                    |
                    v
        +------------------------------+
        |      API - FastAPI (Nuvem)   |
        | - Consome dados da Embrapa   |
        | - Disponibiliza dados (JSON) |
        | - Endpoints documentados     |
        | - (Opcional) Autenticação JWT|
        +---------------+--------------+
                        |
                        v
           +-------------------------------+
           |       Banco de Dados (Cloud)  |
           | - PostgreSQL / MongoDB        |
           | - Dados estruturados          |
           +---------------+---------------+
                           |
                           v
           +-------------------------------+
           | Pipeline de Machine Learning  |
           | - Coleta dados do DB          |
           | - Treinamento e inferência    |
           | - Salva previsões no DB       |
           +-------------------------------+
```

## ⚙️ Componentes

### 1️⃣ Ingestão de Dados
- **Fonte:** Site da Embrapa (via requisicao HTTP).
- **Processo:**
  - Coleta via requisicao HTTPS dos dados das abas:
    - Produção
    - Processamento
    - Comercialização
    - Importação
    - Exportação
  - Transformação dos dados brutos em dados estruturados (Json).
- **Destino:** Pipeline de Machine Learning.

---

### 2️⃣ API (FastAPI)
- **Funções principais:**
  - Consumir APIs públicas.
  - Fornecer endpoints REST para:
    - Consultar dados.
  - Documentação automática disponível em `/docs`.
  - Autenticação via JWT.
- **Tecnologias:**
  - Python + FastAPI.
  - Pydantic para validação de dados.
  - SQLAlchemy (PostgreSQL).

---

### 3️⃣ Banco de Dados
- **Responsável por armazenar:**
  - Armazena usuário cadastrados para acesso a API.
- **Banco:**
  - PostgreSQL (relacional).
- **Hospedagem:**
  - AWS - Amazon RDS.

---

### 4️⃣ Pipeline de Machine Learning
- **Pipeline Offline:**
  - Extração dos dados do banco.
  - Processamento, feature engineering e limpeza.
  - Treinamento de modelos preditivos (ex.: regressão, árvore, redes neurais).
  - Validação e salvamento dos modelos.
- **Pipeline Online (Opcional):**
  - Deploy do modelo na própria API como endpoint `/predict`.
  - Ou execução periódica que gera previsões e salva no banco.

---

## 🌐 Infraestrutura para Deploy

### 🚢 Containerização
- Criação de **Dockerfile** para empacotar a API.
- **Docker Compose** para ambiente local, contendo:
  - API FastAPI.
  - Banco de dados (PostgreSQL ou MongoDB).

---

### ☁️ Deploy em Nuvem
- **Plataformas recomendadas:**
  - Render.com
  - Railway.app
  - Fly.io
  - Heroku (para MVP)
- **Configurações:**
  - Variáveis de ambiente sensíveis:
    - `DB_URL`
    - `SECRET_KEY` (JWT)
    - `SITE_URL_EMBRAPA`
- **Integração com GitHub Actions (opcional):**
  - Deploy automático a cada push no `main`.

---

### 📊 Monitoramento e Logs
- Logs da API e containers:
  - Ferramentas sugeridas:
    - Logtail
    - Grafana Cloud + Loki
    - Axiom
- Implementação de healthchecks:
  - Endpoint `/health` para status da API.

---

## 🔗 Fluxo Completo do Sistema

```plaintext
[Embrapa] 
   ↓ (Scraping/API)
[API FastAPI]
   ↓ (POST dados)
[Banco de Dados]
   ↓ (Dataset limpo)
[Pipeline ML]
   ↓ (Previsões e análises)
[Banco de Dados]
   ↑ (GET previsões)
[API → Usuário Final]

```

## 🧠 Cenário de Machine Learning (Exemplo)

- **Problema:** Previsão da produção de vinho nos próximos anos.
- **Input:** Dados históricos de:
  - Produção
  - Clima
  - Comercialização
  - Importação
  - Exportação
- **Output:**
  - Previsões de produção futura.
  - Análise de tendências de mercado.
- **Entrega:**
  - Endpoint na API `/predict` com dados de entrada dinâmicos.
  - Ou execução periódica que salva previsões no banco para consultas futuras.

---

## 📦 Estrutura do Repositório (Exemplo)

```plaintext
├── app/
│   ├── main.py                # Arquivo principal da API
│   ├── api/                   # Rotas e endpoints
│   ├── models/                # Models do banco
│   ├── services/              # Lógica de scraping e ingestão
│   ├── utils/                 # Funções auxiliares
│   └── schemas/               # Schemas Pydantic
├── ml/
│   ├── pipeline.py            # Pipeline de dados para ML
│   ├── model.pkl              # Modelo treinado
│   └── predict.py             # Script de predição
├── Dockerfile                 # Dockerfile da API
├── docker-compose.yml         # Compose para API + DB
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação do projeto
```


