# sdd-task-analyzer

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![Test Harness](https://img.shields.io/badge/tests-pytest-green)
![Methodology](https://img.shields.io/badge/methodology-SDD%20%2F%20AI%20Governance-orange)

## 📌 Descrição do Projeto

O **TaskAnalyzer** é um módulo de software especializado em análise estatística e métricas de produtividade para gestão de tarefas. O projeto foi desenvolvido utilizando a metodologia **Spec-Driven Development (SDD)** e guiado por regras estritas de governança de IA (`CONTEXT_RULES.md`) para garantir a consistência e integridade do código.

O módulo processa lotes de dados contendo tarefas concluídas e pendentes, gerando indicadores como tempo médio de conclusão (geral e por prioridade), totalizadores e taxa de atraso.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Testes Automatizados:** Pytest
- **Gestão e Versionamento:** Git & GitHub
- **Desenvolvimento Assistido:** Assistente de IA com governança de contexto

---

## 📂 Estrutura do Repositório

```text
sdd-task-analyzer/
├── README.md                 # Documentação geral do projeto
├── CONTEXT_RULES.md          # Regras de governança e restrições para a IA
├── .gitignore                # Ficheiros ignorados pelo Git
├── requirements.txt          # Dependências do projeto (pytest)
├── specs/
│   └── task_analyzer_spec.md # Contrato de especificação técnica SDD
├── src/
│   └── task_analyzer.py      # Implementação do algoritmo e exceções
└── tests/
    └── test_harness.py       # Suíte de testes automatizados com pytest
```