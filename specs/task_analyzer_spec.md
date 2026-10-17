# Especificação do Contrato SDD — TaskAnalyzer

## 1. Visão Geral
O `TaskAnalyzer` processa lotes de tarefas para calcular métricas estatísticas de produtividade[cite: 2].

## 2. Contrato de Entrada (Inputs)
Cada tarefa no lote deve conter os seguintes campos[cite: 2]:
- `id` (int): Identificador único positivo[cite: 2].
- `titulo` (str): Nome da tarefa (não vazio)[cite: 2].
- `prioridade` (str): Nível (`alta`, `media`, `baixa`)[cite: 2].
- `data_criacao` (str/datetime): Formato ISO 8601 se string[cite: 2].
- `data_conclusao` (str/datetime/None): Formato ISO 8601 se string. Obrigatório para `concluido`, `None` para `pendente`[cite: 2].
- `status` (str): `concluido` ou `pendente`[cite: 2].

## 3. Contrato de Saída (Outputs)
O retorno da função `analyze_tasks` deve seguir a estrutura[cite: 2]:
```json
{
  "total_geral": int,
  "total_concluidas": int,
  "total_pendentes": int,
  "tempo_medio_conclusao_dias": float,
  "taxa_atraso_percentual": float,
  "indicadores_por_prioridade": {
    "alta": {"total": int, "concluidas": int, "tempo_medio_dias": float},
    "media": {"total": int, "concluidas": int, "tempo_medio_dias": float},
    "baixa": {"total": int, "concluidas": int, "tempo_medio_dias": float}
  }
}