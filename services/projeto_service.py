from database import get_session
from models import Projeto, Tarefa
from schemas.projeto_schemas import CriarProjetoSchema


def listar_projeots() -> list[dict[str, object]]:
    with get_session() as session:
        todos_projetos = session.query(Projeto).order_by(Projeto.id.desc()).all()
        return [p.to_dict() for p in todos_projetos]


def criar_projeto(data: CriarProjetoSchema) -> dict[str, object]:
    print(f"Criando projeto - data: {data}")
    with get_session() as session:
        projeto = Projeto(
            emoji=data.emoji,
            nome=data.nome,
            descricao=data.descricao,
            valor=data.valor,
            template_id=data.template,
            status=data.status,
        )
        session.add(projeto)
        session.flush()

        tarefas = data.tarefas or []
        tarefas_do_projeto = [
            Tarefa(
                nome=t.nome,
                feito=bool(t.feito or False),
                projeto_id=projeto.id,
            )
            for t in tarefas
        ]
        session.add_all(tarefas_do_projeto)

        session.commit()
        return projeto.to_dict()


def atualizar_projeto(
    projeto_id: int, data: CriarProjetoSchema
) -> dict[str, object] | None:
    print(f"Atualizando projeto: {projeto_id}, {data}")
    with get_session() as session:
        projeto = session.query(Projeto).filter(Projeto.id == projeto_id).first()
        if not projeto:
            return None

        for field, value in data.items():
            if field == "template":
                projeto.template_id = value
                continue

            if field != "tarefas":
                setattr(projeto, field, value)

        if "tarefas" in data:
            tarefas = data["tarefas"] or []
            session.query(Tarefa).filter_by(projeto_id=projeto.id).delete()
            session.flush()
            tarefas_novas = [
                Tarefa(
                    nome=t["nome"],
                    feito=bool(t.get("feito", False)),
                    projeto_id=projeto.id,
                )
                for t in tarefas
            ]
            session.add_all(tarefas_novas)

        session.commit()
        return projeto.to_dict()


def deletar_projeto(projeto_id: int) -> bool:
    print(f"Deletando projeto: {projeto_id}")
    with get_session() as session:
        projeto = session.query(Projeto).filter(Projeto.id == projeto_id).first()
        if not projeto:
            return False
        session.delete(projeto)
        session.commit()
        return True
