import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.INFO)
Logger = logging.getLogger(__name__)


class TaskValidationError(ValueError):
    """Exceção customizada para erros de validação nas tarefas."""
    pass


def ParseDatetime(Value: Any) -> datetime:
    if isinstance(Value, datetime):
        return Value
    if isinstance(Value, str):
        return datetime.fromisoformat(Value)
    raise TaskValidationError(f"Formato de data inválido: {Value}")


def AnalyzeTasks(Tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analisa um lote de tarefas e gera indicadores estatísticos."""
    Logger.info("Iniciando análise de %d tarefas.", len(Tasks))

    Metrics: Dict[str, Any] = {
        "total_geral": len(Tasks),
        "total_concluidas": 0,
        "total_pendentes": 0,
        "tempo_medio_conclusao_dias": 0.0,
        "taxa_atraso_percentual": 0.0,
        "indicadores_por_prioridade": {
            "alta": {"total": 0, "concluidas": 0, "tempo_medio_dias": 0.0},
            "media": {"total": 0, "concluidas": 0, "tempo_medio_dias": 0.0},
            "baixa": {"total": 0, "concluidas": 0, "tempo_medio_dias": 0.0},
        },
    }

    if not Tasks:
        return Metrics

    TotalCompletionDays: float = 0.0
    PriorityCompletionDays: Dict[str, float] = {"alta": 0.0, "media": 0.0, "baixa": 0.0}
    DelayedTasksCount: int = 0

    for Task in Tasks:
        TaskId: int = Task.get("id", 0)
        Status: str = Task.get("status", "").lower()
        Priority: str = Task.get("prioridade", "").lower()

        if Priority in Metrics["indicadores_por_prioridade"]:
            Metrics["indicadores_por_prioridade"][Priority]["total"] += 1

        if Status == "pendente":
            Metrics["total_pendentes"] += 1
        elif Status == "concluido":
            Metrics["total_concluidas"] += 1
            if Priority in Metrics["indicadores_por_prioridade"]:
                Metrics["indicadores_por_prioridade"][Priority]["concluidas"] += 1

            CreationDate: datetime = ParseDatetime(Task.get("data_criacao"))
            CompletionDate: Optional[datetime] = ParseDatetime(Task.get("data_conclusao")) if Task.get("data_conclusao") else None

            if CompletionDate:
                if CompletionDate < CreationDate:
                    ErrorMessage: str = f"Data de conclusão não pode ser anterior à data de criação na tarefa ID {TaskId}"
                    Logger.error(ErrorMessage)
                    raise TaskValidationError(ErrorMessage)

                DaysToComplete: float = (CompletionDate - CreationDate).total_seconds() / 86400.0
                TotalCompletionDays += DaysToComplete

                if Priority in PriorityCompletionDays:
                    PriorityCompletionDays[Priority] += DaysToComplete

                if Task.get("atrasada", False):
                    DelayedTasksCount += 1

    TotalCompleted: int = Metrics["total_concluidas"]
    if TotalCompleted > 0:
        Metrics["tempo_medio_conclusao_dias"] = round(TotalCompletionDays / TotalCompleted, 2)
        Metrics["taxa_atraso_percentual"] = round((DelayedTasksCount / TotalCompleted) * 100.0, 2)

        for PriorityKey in ["alta", "media", "baixa"]:
            CompletedInPriority: int = Metrics["indicadores_por_prioridade"][PriorityKey]["concluidas"]
            if CompletedInPriority > 0:
                AvgDays: float = PriorityCompletionDays[PriorityKey] / CompletedInPriority
                Metrics["indicadores_por_prioridade"][PriorityKey]["tempo_medio_dias"] = round(AvgDays, 2)

    return Metrics