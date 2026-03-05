# Pizzaria AI

Projeto de estudo e experimentação focado na construção de um sistema de atendimento automatizado para uma pizzaria utilizando **LLMs, agentes e arquitetura de APIs modernas**.

A aplicação simula um sistema real de pedidos onde um **agente de IA interpreta pedidos em linguagem natural**, interage com o backend e gerencia pedidos de clientes.

Este projeto tem como objetivo explorar **arquiteturas modernas envolvendo LLMs, APIs e automação de atendimento**.

---

# Objetivo

Compreender como integrar **modelos de linguagem, agentes e APIs backend** para construir sistemas capazes de interpretar linguagem natural e executar ações reais.

O projeto busca consolidar conhecimentos em:

* **Arquitetura de APIs com FastAPI**
* **Integração de LLMs em aplicações reais**
* **Construção de agentes com ferramentas (tools)**
* **Modelagem de dados e persistência**
* **Integração entre frontend, backend e IA**

Mais do que apenas código, o foco é **entender decisões arquiteturais, trade-offs e padrões utilizados em aplicações reais de IA**.

---

# Estrutura do Projeto

```
pizzaria-ai/

backend/
├── alembic/                # Controle de migrations do banco
├── core/                   # Configurações da aplicação
├── models/                 # Modelos do banco de dados
├── routes/                 # Endpoints da API
├── schemas/                # Schemas de validação (Pydantic)
├── security/               # Autenticação e segurança
├── service/                # Lógica de negócio
│
├── main.py                 # Inicialização da API FastAPI
├── alembic.ini             # Configuração do Alembic
└── requirements.txt        # Dependências do projeto

frontend/
└── (em desenvolvimento)

README.md
```

A arquitetura segue uma separação clara entre:

* **Camada de API**
* **Camada de serviço**
* **Modelos de dados**
* **Integração com IA**

---

# Como Funciona

O sistema simula o fluxo completo de um atendimento automatizado.

### Fluxo de interação

```
Usuário
   ↓
Interface (chat ou frontend)
   ↓
API FastAPI
   ↓
Agente LLM interpreta o pedido
   ↓
Backend executa a ação
   ↓
Pedido registrado no sistema
```

Exemplo de interação:

```
Usuário: Quero uma pizza de calabresa grande e uma coca.

Agente:
- interpreta o pedido
- identifica itens
- valida com o cardápio
- cria o pedido no sistema
```

---

# Arquitetura

O projeto segue uma arquitetura modular inspirada em aplicações modernas de IA.

```
Frontend
   ↓
FastAPI
   ↓
Service
   ↓
Agent 
   ↓
Database
```

### Componentes principais

**API (FastAPI)**
Responsável por expor endpoints HTTP e coordenar as requisições.

**Service Layer**
Contém a lógica de negócio da aplicação (criação de pedidos, consulta de cardápio, etc).

**Agent Layer**
Responsável por interpretar linguagem natural e decidir quais ações executar.

**Database**
Armazena pedidos, itens e outras informações do sistema.

---

# Tecnologias Utilizadas

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Alembic**
* **Pydantic**

### Inteligência Artificial

* **LLM API (OpenAI / Google / outros)**
* **Agentes com ferramentas**
* **Prompt Engineering**

### Infraestrutura

* SQLite (ambiente local)
* Git / GitHub

---

# Roadmap do Projeto

## Fase 1 — Backend Base

* [x] Estrutura inicial do projeto
* [x] Configuração do banco
* [x] Sistema de migrations
* [x] Estrutura de rotas
* [x] CRUD de pedidos
* [ ] CRUD de Produtos

---

## Fase 2 — Integração com IA

* [ ] Agente capaz de interpretar pedidos
* [ ] Tools para criação de pedidos
* [ ] Validação automática de itens
* [ ] Memória de conversa

---

## Fase 3 — Interface do Usuário

* [ ] Interface de chat
* [ ] Página de cardápio
* [ ] Histórico de pedidos

---

# Objetivo do Projeto

Este projeto faz parte de uma jornada de aprendizado focada em:

* **Arquitetura de sistemas com IA**
* **Integração de LLMs em aplicações reais**
* **Construção de agentes capazes de executar tarefas**

A ideia é evoluir gradualmente o sistema até chegar a um **protótipo funcional de atendimento automatizado para restaurantes**.

---

# Sobre

Este repositório documenta o desenvolvimento de um sistema que combina **backend moderno, inteligência artificial e automação de atendimento**.

O objetivo é construir uma compreensão prática de como **LLMs podem ser integrados em aplicações reais**, indo além de simples experimentos e explorando **arquitetura e design de sistemas**.
