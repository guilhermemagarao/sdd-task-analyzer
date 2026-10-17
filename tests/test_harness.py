from datetime import datetime
import pytest
from src.task_analyzer import AnalyzeTasks, TaskValidationError


def test_scenario_1_success():
    """Valida cálculo de métricas com dados válidos (Cenário 1)."""
    Tasks = [
        {
            "id": 101,
            "titulo": "Tarefa 1",
            "prioridade": "alta",
            "data_criacao": "2026-03-01T08:00:00",
            "data_conclusao": "2026-03-03T08:00:00",
            "status": "concluido",
        },
        {
            "id": 102,
            "titulo": "Tarefa 2",
            "prioridade": "alta",
            "data_criacao": "2026-03-01T08:00:00",
            "data_conclusao": "2026-03-05T08:00:00",
            "status": "concluido",
        },
        {
            "id": 103,
            "titulo": "Tarefa 3",
            "prioridade": "media",
            "data_criacao": "2026-03-02T10:00:00",
            "data_conclusao": None,
            "status": "pendente",
        },
    ]

    Result = AnalyzeTasks(Tasks)

    assert Result["total_geral"] == 3
    assert Result["total_concluidas"] == 2
    assert Result["total_pendentes"] == 1
    assert Result["tempo_medio_conclusao_dias"] == 3.0
    assert Result["indicadores_por_prioridade"]["alta"]["tempo_medio_dias"] == 3.0
    assert Result["indicadores_por_prioridade"]["media"]["total"] == 1


def test_scenario_2_invalid_dates():
    """Valida se lança exceção em tarefas com data inconsistente (Cenário 2)."""
    Tasks = [
        {
            "id": 201,
            "titulo": "Tarefa Invalida",
            "prioridade": "alta",
            "data_criacao": "2026-03-10T10:00:00",
            "data_conclusao": "2026-03-01T10:00:00",
            "status": "concluido",
        }
    ]

    with pytest.raises((ValueError, TaskValidationError)) as ExcInfo:
        AnalyzeTasks(Tasks)

    assert "201" in str(ExcInfo.value)


def test_scenario_3_edge_cases():
    """Valida comportamento em listas vazias ou sem concluídas (Cenário 3)."""
    EmptyResult = AnalyzeTasks([])
    assert EmptyResult["total_geral"] == 0
    assert EmptyResult["tempo_medio_conclusao_dias"] == 0.0

    PendingTasks = [
        {
            "id": 301,
            "titulo": "Pendente",
            "prioridade": "baixa",
            "data_criacao": "2026-03-01T10:00:00",
            "data_conclusao": None,
            "status": "pendente",
        }
    ]
    PendingResult = AnalyzeTasks(PendingTasks)
    assert PendingResult["total_geral"] == 1
    assert PendingResult["total_concluidas"] == 0
    assert PendingResult["tempo_medio_conclusao_dias"] == 0.0