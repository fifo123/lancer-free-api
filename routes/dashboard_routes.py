from flask_openapi3 import APIBlueprint, Tag
from services.dashboard_service import listar_dashboard_projetos
from schemas import (
    SomatorioPorStatusSchema,
)

tag = Tag(name="Dashboard", description="Rotas de dashboard")
dashboard_bp = APIBlueprint(
    "Dashboard", __name__, url_prefix="/dashboard", abp_tags=[tag]
)


@dashboard_bp.get(
    "projetos",
    description="Retorna os valores referente aos projetos",
    summary="Lista um somatório dos valores de todos os projetos, agrupando-os pelo seu status, além de retornar o valor total.",
    responses={
        200: SomatorioPorStatusSchema,
    },
)
def rota_listar_dashboard_projetos():
    return listar_dashboard_projetos()
