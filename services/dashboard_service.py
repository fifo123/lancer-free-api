from sqlalchemy import func
from database import get_session
from models import Projeto
from schemas.dashboard_schemas import SomatorioPorStatusSchema


def listar_dashboard_projetos() -> SomatorioPorStatusSchema:
    with get_session() as session:
        soma_por_status = (
            session.query(Projeto.status, func.sum(Projeto.valor).label("valor_total"))
            .group_by(Projeto.status)
            .all()
        )
        total_geral = session.query(
            func.sum(Projeto.valor).label("valor_total")
        ).scalar()

        resultado = {}
        resultado["status"] = {
            status: float(total) for status, total in soma_por_status
        }
        resultado["total"] = float(total_geral or 0)
        return resultado
