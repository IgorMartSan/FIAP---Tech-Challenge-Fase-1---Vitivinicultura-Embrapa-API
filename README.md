# ✅ Entregáveis do Projeto

- [x] API funcional com endpoints REST públicos e documentados.
- [x] Autenticação via JWT. (Opicional)
- [x] Documentação dos endpoints via Swagger (`/docs`).
- [ ] Pipeline de ingestão e processamento funcionando.(Opicional)
- [x] Descrição clara da integração com Machine Learning.
- [x] Diagrama da arquitetura adicionado no README.
- [x] Link do deploy funcionando.


# ✅ Acesso a API

Para autenticar na API e utilizar os endpoints disponíveis, utilize as seguintes credenciais padrão:

Nome de Usuário: admin

Senha: automate123.

# 🏗️ Plano de Deploy — API de Vitivinicultura + ML

## 🔥 Descrição do Projeto
Desenvolvimento de uma API com **FastAPI** que disponibiliza dados públicos de vitivinicultura da **Embrapa**.  
A API irá alimentar uma pipeline de **Machine Learning**.

---

## 🚀 Arquitetura do Projeto

![Diagrama de Exemplo](./architecture.svg)

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
  - Transformação dos dados brutos em dados estruturados (JSON).
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
  - AWS - EC2.
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

### 4️⃣ Pipeline de Machine Learning (Opicional)
- **Pipeline Offline:**
  - Armazenamento dos Dados.
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
[Pipeline ML]
   ↓ (Dataset de treino, Previsões e análises)
[API Deploy]
   ↓ (Previsões)   
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



