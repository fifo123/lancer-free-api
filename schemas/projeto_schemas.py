from enum import Enum
from typing import ClassVar, List
from pydantic import BaseModel, ConfigDict
from pydantic import Field, StringConstraints, condecimal
from typing import Annotated
from decimal import Decimal


class ProjetoPath(BaseModel):
    projeto_id: int = Field(..., description="id do projeto")


class TarefaProjetoSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)

    nome: Annotated[str, StringConstraints(min_length=1, max_length=200)]
    feito: bool = False


class StatusProjetoEnum(str, Enum):
    pending = "pending"
    progress = "progress"
    done = "done"


class EmojiEnum(str, Enum):
    SORRISO = "😀"
    RISO = "😂"
    APAIXONADO = "😍"
    OCULOS_ESCUROS = "😎"
    CHORANDO = "😢"
    BRAVO = "😡"
    JOINHA = "👍"
    ORACAO = "🙏"
    FESTA = "🎉"
    FOGO = "🔥"
    CACHORRO = "🐶"
    GATO = "🐱"
    RAPOSA = "🦊"
    PANDA = "🐼"
    MACACO = "🐵"
    LEAO = "🦁"
    SAPO = "🐸"
    PINGUIM = "🐧"
    TARTARUGA = "🐢"
    POLVO = "🐙"
    MACA = "🍎"
    HAMBURGUER = "🍔"
    PIZZA = "🍕"
    SUSHI = "🍣"
    DONUT = "🍩"
    CHOCOLATE = "🍫"
    CERVEJA = "🍺"
    VINHO = "🍷"
    CAFE = "☕"
    REFRI = "🥤"
    FUTEBOL = "⚽"
    BASQUETE = "🏀"
    FUTEBOL_AMERICANO = "🏈"
    TENIS = "🎾"
    PING_PONG = "🏓"
    VIDEOGAME = "🎮"
    DADO = "🎲"
    MUSICA = "🎵"
    VIOLAO = "🎸"
    MICROFONE = "🎤"
    CARRO = "🚗"
    AVIAO = "✈️"
    FOGUETE = "🚀"
    BICICLETA = "🚲"
    CASA = "🏠"
    PRAIA = "🏖️"
    MONTANHA = "🏔️"
    ESTATUA_LIBERDADE = "🗽"
    VULCAO = "🌋"
    CASTELO = "🏰"
    CORACAO = "❤️"
    CORACAO_PARTIDO = "💔"
    CEM_POR_CENTO = "💯"
    BRILHO = "✨"
    LUA = "🌙"
    ESTRELA = "⭐"
    ARCO_IRIS = "🌈"
    SOL = "☀️"
    CHUVA = "🌧️"
    NEVE = "❄️"


class CriarProjetoSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)

    emoji: Annotated[EmojiEnum, StringConstraints(min_length=1, max_length=8)] = (
        EmojiEnum.CASTELO
    )
    nome: Annotated[str, StringConstraints(min_length=1, max_length=200)]
    descricao: Annotated[str, StringConstraints(min_length=1, max_length=500)]
    status: Annotated[
        StatusProjetoEnum, StringConstraints(min_length=1, max_length=100)
    ] = StatusProjetoEnum.pending
    valor: Annotated[Decimal, condecimal(max_digits=12, decimal_places=2)]
    template: str | int | None = None
    tarefas: list[TarefaProjetoSchema] = Field(default_factory=list)


class ProjetoSchema(BaseModel):
    emoji: Annotated[EmojiEnum, StringConstraints(min_length=1, max_length=8)] = (
        EmojiEnum.CASTELO
    )
    nome: Annotated[str, StringConstraints(min_length=1, max_length=200)]
    descricao: Annotated[str, StringConstraints(min_length=1, max_length=500)]
    status: Annotated[
        StatusProjetoEnum, StringConstraints(min_length=1, max_length=100)
    ] = StatusProjetoEnum.pending
    valor: Annotated[Decimal, condecimal(max_digits=12, decimal_places=2)]
    template: str | int | None = None
    tarefas: list[TarefaProjetoSchema] = Field(default_factory=list)


class ProjetoListagemSchema(BaseModel):
    projetos: List[ProjetoSchema]


class ProjetoDeletadoResponse(BaseModel):
    message: str
