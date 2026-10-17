# CONTEXT RULES — Governança para Agentes de IA

Este documento contém as diretrizes que devem ser estritamente seguidas por qualquer assistente de IA durante o desenvolvimento do projeto TaskAnalyzer.

## 1. Diretrizes Arquiteturais
- **Linguagem:** Python 3.11+.
- **Tipagem Estática:** Type hints obrigatórios em 100% das funções e parâmetros.
- **Estilo de Código:** Padrão PEP 8 e princípios de Single Responsibility (SRP).
- **Documentação:** Google style docstrings em módulos, classes e funções[cite: 2].
- **Tratamento de Erros:** Exceções específicas e prevenção contra divisão por zero (`ZeroDivisionError`).
- **Logs:** Utilização do módulo nativo `logging`.

## 2. Proibições Estritas
- Não utilizar bibliotecas externas não autorizadas (ex.: utilizar apenas a biblioteca padrão e `pytest`).
- Não alterar, remover ou adaptar a suíte de testes.
- Não modificar a estrutura de pastas do repositório.
- Não persistir dados em disco ou base de dados.
- Não alterar a assinatura pública da função `analyze_tasks`.

## 3. Fluxo de Interação
- Toda a geração de código deve respeitar a especificação funcional em `specs/task_analyzer_spec.md`.
- Em caso de falha nos testes, o agente deve receber o traceback do `pytest` para efetuar a autocorreção sem alterar os testes.