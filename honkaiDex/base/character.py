
from dataclasses import dataclass
import dataclasses
import typing


class BaseCharacterMeta(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

@dataclass
class BaseCharacter(metaclass=BaseCharacterMeta):
    _name : str
    _nicknames : typing.List[str] = dataclasses.field(default_factory=lambda : [])

from enum import Enum
class CharacterTag(Enum):
    Physical = 1
    Burst = 2
    Fire = 3
    Ice = 4
    Lightning = 5
    Freeze = 6
    Paralyze = 7
    Stun = 8
    Ignite = 9
    Bleed = 10
    Heavy = 11
    Weaken = 12
    Impair = 13
    Time = 14
    Gather = 15
    Heal = 16
    Fast = 17
    Aerial = 18

    @staticmethod
    def get(name : str):
        name = name.lower()
        name = name[0].upper() + name[1:]

        for tag in CharacterTag:
            if tag.name == name:
                return tag
        return None


class BattlesuitMeta(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]

@dataclass
class Battlesuit(metaclass=BattlesuitMeta):
    _base_character : BaseCharacter
    _unlock_shards : int
    _name : str
    _version_released : float
    _rairty : str
    _tags : typing.List[CharacterTag] = dataclasses.field(default_factory=lambda : [])
    _img_link : str = None
    _else : dict = dataclasses.field(default_factory=lambda : {})
