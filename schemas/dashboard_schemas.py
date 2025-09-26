from pydantic import BaseModel, Field
from typing import Dict


class SomatorioPorStatusSchema(BaseModel):
    total: float = Field(..., description="Somatório total de todos os projetos")
    status: Dict[str, float] = Field(
        ...,
        description="Dicionário com o somatório de cada status. Chave = status do projeto, Valor = somatório de 'valor'",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "total": 6000.0,
                "status": {"pending": 1000.0, "done": 5000.0},
            }
        }
