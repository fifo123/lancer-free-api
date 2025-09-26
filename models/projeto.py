from typing import ClassVar
from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base
from models.tarefa import Tarefa
from models.template import Template


class Projeto(Base):
    __tablename__: ClassVar[str] = "projetos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    emoji: Mapped[str] = mapped_column(String(8), nullable=False)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    descricao: Mapped[str] = mapped_column(String(500), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(100), nullable=False)
    template_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("templates.id"), nullable=True
    )

    template: Mapped[Template | None] = relationship("Template", backref="projetos")
    tarefas: Mapped[list[Tarefa]] = relationship(
        "Tarefa", cascade="all, delete-orphan", backref="projeto", lazy="joined"
    )

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "emoji": self.emoji,
            "nome": self.nome,
            "descricao": self.descricao,
            "status": self.status,
            "valor": float(self.valor),
            "template": self.template_id or "none",
            "tarefas": [t.to_dict() for t in self.tarefas or []],
        }
