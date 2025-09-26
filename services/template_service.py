from database import get_session
from models import Template
from schemas.template_schemas import CriarTemplateSchema


def listar_templates():
    with get_session() as session:
        return [
            t.to_dict()
            for t in session.query(Template).order_by(Template.id.desc()).all()
        ]


def criar_template(data: CriarTemplateSchema):
    print(f"Criando template: {data}")
    with get_session() as session:
        tpl = Template(
            nome=data.nome,
            descricao=data.descricao,
            tarefas=[t.__dict__ for t in data.tarefas],
        )
        session.add(tpl)
        session.commit()
        return tpl.to_dict()


def atualizar_template(template_id: int, data: CriarTemplateSchema):
    print(f"Atualizando template: {template_id}, {data}")
    with get_session() as session:
        tpl = session.query(Template).filter(Template.id == template_id).first()
        if not tpl:
            return None
        for field, value in data.items():
            setattr(tpl, field, value)
        session.commit()
        return tpl.to_dict()
