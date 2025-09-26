from flask_openapi3 import APIBlueprint, Tag
from services.template_service import (
    listar_templates,
    criar_template,
    atualizar_template,
)
from schemas import (
    CriarTemplateSchema,
    TemplateListagemSchema,
    TemplatePath,
    TemplateSchema,
)

tag = Tag(name="Templates", description="CRUD de Templates")
template_bp = APIBlueprint(
    "Templates", __name__, url_prefix="/templates", abp_tags=[tag]
)


@template_bp.get(
    "",
    description="Retorna todos os templates disponíveis no banco",
    summary="Lista todos os templates",
    responses={200: TemplateListagemSchema},
)
def rota_listar_todos_templates() -> TemplateListagemSchema:
    templates = listar_templates()
    return {"templates": templates}


@template_bp.post(
    "",
    description="Cria um novo template para ser utilizado nos projetos",
    summary="Cria um novo template",
    responses={200: TemplateSchema},
)
def rota_criar_template(body: CriarTemplateSchema):
    tpl = criar_template(body)
    return tpl, 200


@template_bp.put(
    "/<int:template_id>",
    description="Atualiza um template, as tarefas adicionadas não afetam o projeto",
    summary="Atualiza um template",
    responses={200: TemplateSchema},
)
def rota_editar_template(path: TemplatePath, body: CriarTemplateSchema):
    proj = atualizar_template(path.template_id, body.model_dump(exclude_unset=True))
    if proj is None:
        return {"error": "Projeto não encontrado"}, 404
    return proj, 200
