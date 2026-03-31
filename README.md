# Plataforma de Governança de Mudanças com AIOps

Plataforma de governança DevOps orientada por AIOps para análise automática de risco de mudanças, validação de políticas e geração inteligente de evidências de auditoria em pipelines de CI/CD.

Este projeto visa aplicar **conceitos de AIOps à governança DevOps**, permitindo tomada de decisão inteligente durante o ciclo de entrega de software.

A plataforma integra pipelines de CI/CD com análise baseada em IA para avaliar o **risco de mudanças de código**, aplicar políticas de governança e gerar automaticamente **evidências para auditoria**.

---

# Visão Geral

Pipelines modernos de DevOps automatizam build e deploy, porém **governança de mudanças e análise de risco** quando existem, ainda são frequentemente manuais ou baseadas apenas em regras.

Este projeto explora como **AIOps (Artificial Intelligence for IT Operations)** pode melhorar a governança DevOps por meio de:

- análise automática de risco de mudanças
- validação inteligente de políticas
- geração automática de evidências de auditoria
- tomada de decisão assistida por IA

O objetivo é simular uma **Plataforma Inteligente de Governança de Mudanças**, semelhante ao que ambientes corporativos utilizam para controlar deploys e reduzir riscos operacionais.

---

# Arquitetura

A solução integra ferramentas de CI/CD com uma camada de governança baseada em IA.

Eventos do pipeline são enviados para agentes de IA responsáveis por classificar mudanças, calcular risco e tomar decisões de governança.

Fluxo de alto nível:
- Preparar um diagrama no Draw.io depois.

1. Desenvolvedor
2. Repositório GitLab
3. Pipeline Jenkins
4. Build + Análise de Código (SonarQube)
5. Agente de Governança com IA
6. Motor de Decisão (Aprovar / Revisar / Bloquear)
7. Geração de Evidência de Auditoria

---

# Funcionalidades Principais

## Análise de Risco de Mudança

Avalia commits e eventos do pipeline para determinar o nível de risco da alteração.

## Classificação de Mudanças

Classificação automática de commits, como por exemplo:

- bugfix
- feature
- refactor
- security
- infraestrutura

## Motor de Decisão de Governança

Aplica regras e análise de risco para determinar:

- **APROVAR**
- **REVISÃO NECESSÁRIA**
- **BLOQUEAR**

## Geração Automática de Evidências

Gera evidências estruturadas que podem ser utilizadas para **auditoria e compliance**.

## Integração com CI/CD

Integração com ferramentas comuns do ecossistema DevOps:

- Jenkins
- GitLab
- SonarQube

---

# Estrutura do Projeto

```bash
aiops-change-governance
│
├── architecture
│ ├── diagrams
│ └── decisions
│
├── infrastructure
│ ├── docker-compose
│ └── jenkins
│
├── ai-governance-agent
│
├── demo-app
│ └── springboot-demo
│
├── pipelines
│ └── Jenkinsfile
│
├── docs
│ ├── aiops-model.md
│ ├── governance-model.md
│ └── experiment-results.md
│
└── experiments
├── baseline
└── aiops-version
```


---

# Stack Tecnológica

- CI/CD
    - Jenkins
    - GitLab

- Qualidade de Código
    - SonarQube

- Motor de Governança com IA
    - Python
    - FastAPI

- Infraestrutura
    - Docker
    - Docker Compose

- Aplicação de Exemplo
    - Spring Boot

---

# Executando a Plataforma Localmente

Todo o ambiente pode ser executado localmente usando Docker Compose.

Serviços incluídos:

- GitLab
- Jenkins
- SonarQube
- Agente de Governança com IA
- Aplicação Spring Boot de demonstração

Subir o ambiente:

```bash
docker compose up -d
```

Após iniciar, os serviços estarão disponíveis em:

| Serviço        | URL                                                      |
| -------------- | -------------------------------------------------------- |
| Jenkins        | [http://localhost:8080](http://localhost:8080)           |
| GitLab         | [http://localhost:8081](http://localhost:8081)           |
| SonarQube      | [http://localhost:9000](http://localhost:9000)           |
| API Governança | [http://localhost:8000/docs](http://localhost:8000/docs) |

## Exemplo de Fluxo de Governança

- Depois fazer um diagrama melhor no Draw.io


1. Desenvolvedor realiza push do código no GitLab
2. O pipeline do Jenkins é iniciado
3. O projeto Spring Boot é compilado
4. O SonarQube executa análise de qualidade
5. O pipeline envia dados da mudança para o agente de governança
6. O agente de IA analisa a mudança
7. Uma decisão é retornada ao pipeline
8. Evidências são geradas para auditoria

- Exemplo de resposta da análise:

```json
{
  "change_type": "feature",
  "risk_score": 0.72,
  "risk_level": "HIGH",
  "decision": "REVIEW"
}
```

## Modelos de Governança Comparados

Este projeto explora dois modelos de governança em pipelines DevOps.

1. Governança Tradicional
- validação baseada em regras
- políticas estáticas
- avaliação manual de risco

2. Governança com AIOps
- análise de risco automática
- classificação inteligente de mudanças
- tomada de decisão assistida por IA
- geração automática de evidências

## Objetivo dos Experimentos

- O projeto busca avaliar como AIOps pode melhorar:
    - governança DevOps
    - gestão de risco em mudanças
    - automação de auditoria
    - observabilidade de pipelines

## Próximas Evoluções

- Possíveis evoluções do projeto incluem:
    - detecção de anomalias em pipelines
    - análise de impacto de deploy baseada em métricas
    - arquitetura orientada a eventos com Kafka
    - integração com Prometheus e Grafana
    - uso de modelos de machine learning para previsão de risco


## Artigo Técnico

- Um artigo técnico detalhando arquitetura, implementação e resultados será publicado no Medium.

- **O artigo abordará:**
    - desafios da **governança DevOps**
    - arquitetura baseada em **AIOps**
    - resultados do laboratório
    - aprendizados e próximos passos
- **Autor**: Leonardo Viana
- **DevOps / Platform Engineering**
- **AIOps • Observabilidade • Sistemas Distribuídos**