# Roadmap — Plataforma de Governança de Mudanças com AIOps

Este roadmap descreve a evolução do projeto **AIOps Change Governance Platform**, desde a criação do laboratório DevOps até a implementação de governança inteligente baseada em AIOps.

O objetivo é construir um ambiente experimental que permita comparar **governança tradicional baseada em regras** com **governança inteligente baseada em AIOps**.

---

# Fase 1 — Setup do laboratório

Objetivo: criar o ambiente de experimentação local.

## Atividades

- [x] Criar repositório no GitHub
- [x] Definir estrutura inicial do projeto
- [x] Criar README inicial
- [x] Criar diretórios principais (`architecture`, `docs`, `infrastructure`, `pipelines`)
- [x] Criar arquivo `docker-compose.yml`
- [x] Subir ambiente local com Docker

## Serviços do laboratório

- [x] GitLab
- [x] Jenkins
- [x] SonarQube

## Entregáveis

- [x] Ambiente DevOps funcional rodando localmente
- [x] Estrutura organizada do repositório
- [x] Primeiro commit do projeto

---

# Fase 2 — Aplicação de demonstração

Objetivo: criar um sistema que gere mudanças simuladas para os pipelines.

## Atividades

- [x] Criar projeto demo com Spring Boot
- [x] Criar estrutura básica da API
- [x] Implementar endpoints simples
- [x] Criar Dockerfile da aplicação

## Endpoints sugeridos

- [x] `GET /products`
- [x] `POST /products`
- [x] `GET /health`

## Entregáveis

- [x] Aplicação demo funcional
- [x] Repositório criado no GitLab
- [x] Aplicação pronta para build no pipeline

---

# Fase 3 — Pipeline DevOps

Objetivo: construir pipeline CI/CD para a aplicação demo.

## Atividades

- [x] Criar Jenkinsfile
- [x] Configurar integração Jenkins ↔ GitLab
- [x] Configurar build da aplicação
- [x] Configurar execução de testes
- [x] Configurar análise de qualidade com SonarQube

## Estágios do pipeline

- [x] Checkout
- [x] Build
- [x] Test
- [x] Sonar Analysis
- [x] Package
- [x] Governance Check

## Entregáveis

- [x] Pipeline CI/CD funcional
- [x] Integração completa com GitLab
- [x] Integração com SonarQube

---

# Fase 4 — Governança tradicional (baseline)

Objetivo: criar modelo inicial de governança baseado apenas em regras.

## Atividades

- [ ] Criar serviço simples de governança
- [ ] Implementar validação de commit message
- [ ] Definir limite de arquivos alterados
- [ ] Definir limite de linhas alteradas
- [ ] Validar branch de origem

## Exemplos de regras

- [ ] `files_changed > 50 → REVIEW`
- [ ] `branch != main → BLOCK`

## Entregáveis

- [ ] Serviço de governança rule-based
- [ ] Integração com pipeline Jenkins
- [ ] Decisão automatizada baseada em regras

---

# Fase 5 — Serviço de AIOps

Objetivo: implementar o motor inteligente de governança.

## Atividades

- [x] Criar microserviço Python
- [x] Criar API REST para análise de mudanças
- [x] Estruturar agentes de análise

## Agentes iniciais

### Change Classifier

- [ ] Classificar commits por tipo
- [ ] Categorias: bugfix, feature, refactor, security, infra

### Risk Agent

- [ ] Calcular score de risco
- [ ] Analisar quantidade de arquivos alterados
- [ ] Analisar quantidade de linhas alteradas
- [ ] Considerar tipo de mudança

### Evidence Generator

- [ ] Gerar evidências de auditoria
- [ ] Registrar resultado da análise

## Entregáveis

- [ ] API de governança com IA
- [ ] Integração Jenkins → Serviço de IA

---

# Fase 6 — Decision Engine

Objetivo: transformar análise em decisões automatizadas.

## Atividades

- [ ] Implementar motor de decisão
- [ ] Mapear score de risco para decisões
- [ ] Integrar retorno da decisão ao pipeline

## Regras de decisão

- [ ] LOW → APPROVE
- [ ] MEDIUM → REVIEW
- [ ] HIGH → BLOCK

## Entregáveis

- [ ] Pipeline controlado pela governança
- [ ] Decisão automática baseada na análise de risco

---

# Fase 7 — Auditoria e evidências

Objetivo: registrar evidências das decisões tomadas.

## Atividades

- [ ] Definir modelo de evidência
- [ ] Persistir evidências geradas
- [ ] Criar estrutura de auditoria

## Dados armazenados

- [ ] pipeline_id
- [ ] repository
- [ ] author
- [ ] change_type
- [ ] risk_score
- [ ] decision
- [ ] timestamp

## Entregáveis

- [ ] Trilha de auditoria completa
- [ ] Evidências armazenadas

---

# Fase 8 — Observabilidade da plataforma

Objetivo: monitorar comportamento da governança e pipelines.

## Ferramentas

- Prometheus
- Grafana

## Atividades

- [ ] Coletar métricas do pipeline
- [ ] Coletar métricas da governança
- [ ] Criar dashboards

## Métricas sugeridas

- [ ] pipeline_duration
- [ ] risk_distribution
- [ ] governance_decision_rate

## Entregáveis

- [ ] Dashboards de monitoramento
- [ ] Métricas do sistema de governança

---

# Fase 9 — Arquitetura orientada a eventos (avançado)

Objetivo: evoluir arquitetura para modelo de AIOps orientado a eventos.

## Ferramenta sugerida

Apache Kafka

## Atividades

- [ ] Criar broker de eventos
- [ ] Publicar eventos de pipeline
- [ ] Consumir eventos nos agentes de IA

## Fluxo esperado

Pipeline Event  
↓  
Kafka  
↓  
AI Agents  
↓  
Decision Engine

## Entregáveis

- [ ] Arquitetura event-driven
- [ ] Processamento assíncrono de eventos

---

# Fase 10 — Documentação e artigo técnico

Objetivo: transformar o projeto em material técnico publicável.

## Documentação

- [ ] Criar documentação de arquitetura
- [ ] Documentar modelo AIOps
- [ ] Documentar modelo de governança
- [ ] Documentar experimentos

## Estrutura de documentação

- [ ] `docs/architecture`
- [ ] `docs/aiops-model`
- [ ] `docs/governance-model`
- [ ] `docs/experiment-results`

## Diagramas

- [ ] Diagrama de arquitetura da plataforma
- [ ] Diagrama do fluxo de pipeline
- [ ] Comparação governança tradicional vs AIOps

## Artigo Medium

- [ ] Descrever problema de governança DevOps
- [ ] Explicar abordagem tradicional
- [ ] Apresentar arquitetura AIOps
- [ ] Demonstrar implementação
- [ ] Apresentar resultados do laboratório

---

# Resultado esperado do projeto

Entregáveis:

- [ ] Laboratório DevOps completo
- [ ] Governança baseada em regras
- [ ] Governança baseada em AIOps
- [ ] Arquitetura documentada
- [ ] Evidências de auditoria
- [ ] Observabilidade da plataforma
- [ ] Artigo técnico publicado