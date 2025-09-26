from typing import ClassVar, TypedDict
from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class TarefaTemplate(TypedDict):
    nome: str
    feito: bool


class Template(Base):
    __tablename__: ClassVar[str] = "templates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    descricao: Mapped[str] = mapped_column(String(500), nullable=False)
    tarefas: Mapped[list[TarefaTemplate]] = mapped_column(
        JSON, nullable=False, default=list
    )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "tarefas": self.tarefas or [],
        }
