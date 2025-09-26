from typing import ClassVar
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Tarefa(Base):
    __tablename__: ClassVar[str] = "tarefas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    feito: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    projeto_id: Mapped[int] = mapped_column(ForeignKey("projetos.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "feito": bool(self.feito),
            "projeto_id": self.projeto_id,
        }
