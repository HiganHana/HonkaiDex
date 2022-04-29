from dataclasses import dataclass
import typing
import dataclasses
from zxutil.umodel import UItem, UPrimaryKey, UIterableUniqueKey

@dataclass
class BaseHonkaiModel(UItem):
    name : typing.Union[str, UPrimaryKey]
    nicknames : typing.Union[typing.List[str], UIterableUniqueKey]
    other : typing.Dict[str, typing.Any]

    @classmethod
    def create(cls, **kwargs):
        all_fields = cls.get_stats().all_fields

        other = kwargs.pop("other", {})

        for key, val in kwargs.items():
            if key not in all_fields:
                other[key] = val

        kwargs = {k:v for k,v in kwargs.items() if k in all_fields}

        return super().create(**kwargs, other=other)

@dataclass
class BaseCharacter(BaseHonkaiModel):
    pass

@dataclass
class Battlesuit(BaseHonkaiModel):
    base : BaseCharacter
    version_released : str
    rarity : str
    tags : typing.List[str] = dataclasses.field(default_factory=lambda : [])
    img_link : str = None
    type : typing.Optional[str] = None