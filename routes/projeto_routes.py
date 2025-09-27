from flask_openapi3 import APIBlueprint, Tag
from services.projeto_service import (
    listar_projeots,
    criar_projeto,
    atualizar_projeto,
    deletar_projeto,
)
from schemas import (
    CriarProjetoSchema,
    ProjetoListagemSchema,
    ProjetoPath,
    ProjetoSchema,
    ProjetoDeletadoResponse,
)

tag = Tag(name="Projetos", description="CRUD de Projetos")
projeto_bp = APIBlueprint("Projetos", __name__, url_prefix="/projetos", abp_tags=[tag])


@projeto_bp.get(
    "",
    description="Retorna todos os projetos disponíveis no banco",
    summary="Lista todos os projetos",
    responses={
        200: ProjetoListagemSchema,
    },
)
def rota_listar_todos_projetos():
    projetos = listar_projeots()
    return {"projetos": projetos}


@projeto_bp.post(
    "",
    description="Cria um novo projeto",
    summary="Cria um novo projeto",
    responses={200: ProjetoSchema},
)
def rota_criar_projeto(body: CriarProjetoSchema):
    proj = criar_projeto(body)
    return proj, 200


@projeto_bp.put(
    "/<int:projeto_id>",
    description="Atualiza um projeto",
    summary="Atualiza um projeto",
    responses={200: ProjetoSchema, 404: ProjetoDeletadoResponse},
)
def rota_editar_projeto(path: ProjetoPath, body: CriarProjetoSchema):
    proj = atualizar_projeto(path.projeto_id, body.model_dump())
    if proj is None:
        return {"error": "Projeto não encontrado"}, 404
    return proj, 200


@projeto_bp.delete(
    "/<int:projeto_id>",
    description="Deleta um projeto de forma definitiva e irreversível",
    summary="Deleta um projeto",
    responses={200: ProjetoDeletadoResponse, 404: ProjetoDeletadoResponse},
)
def rota_deletar_projeto(path: ProjetoPath):
    ok = deletar_projeto(path.projeto_id)
    if not ok:
        return {"message": "Projeto não encontrado"}, 404
    return {"message": "Projeto deletado"}, 200
