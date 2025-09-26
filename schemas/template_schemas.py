from typing import ClassVar, Annotated, List
from pydantic import BaseModel, Field, StringConstraints, ConfigDict


class TemplatePath(BaseModel):
    template_id: int = Field(..., description="id do template")


class TarefaBase(BaseModel):
    nome: Annotated[str, StringConstraints(min_length=1, max_length=200)]
    feito: bool = False


class CriarTemplateSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)

    nome: Annotated[str, StringConstraints(min_length=1, max_length=200)]
    descricao: Annotated[str, StringConstraints(min_length=1, max_length=500)]
    tarefas: list[TarefaBase] = Field(default_factory=list)


class TemplateSchema(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    tarefas: list[TarefaBase] | None = None


class TemplateListagemSchema(BaseModel):
    templates: List[TemplateSchema]
