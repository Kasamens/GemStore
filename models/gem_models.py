from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from enum import Enum


class GemClarity(int, Enum):
    SI = "1"
    VS = "2"
    VVS = "3"
    FL = "4"


class GemColor(str, Enum):
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"


class GemType(str, Enum):
    DIAMOND = "DIAMOND"
    RUBY = "RUBY"
    EMERALD = "EMERALD"


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    size: float
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None
    gem_properties: Optional['Gem'] = Relationship(
        back_populates='gem_properties')


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float
    available: bool = True
    gem_type: GemType = GemType.EMERALD

    gem_properties_id: Optional[int] = Field(
        default=None, foreign_key='gemproperties.id')
    gem_properties: Optional[GemProperties] = Relationship(
        back_populates='gem')
