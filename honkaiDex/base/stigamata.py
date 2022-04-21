from dataclasses import dataclass
import typing

class StigPieceMetaClass(type):
    def _to_hash(self, stig_pos : int, stig_set : 'StigamataSet' = None, stig_name : str = None):
        if stig_set is None and stig_name is None:
            raise ValueError("Either stig_set or stig_name is required")
        if stig_set is not None:
            stig_name = stig_set.name

        return hash(str(stig_pos) +"__"+ str(stig_name))

    t_piece = {}
    m_piece = {}
    b_piece = {}

    def __call__(cls, *args, **kwargs):
        if "__stig_pos__" not in kwargs:
            raise ValueError("__stig_pos__ is required")
        if "__stig_set__" not in kwargs:
            raise ValueError("__stig_set__ is required")
        stig_pos = kwargs.get("__stig_pos__", None)
        if stig_pos is None:
            raise ValueError("__stig_pos__ cannot be None")
        if stig_pos < 0 or stig_pos > 3:
            raise ValueError("__stig_pos__ must be between 0 and 3")
        
        stig_set = kwargs.get("__stig_set__", None)
        if stig_set is None or not isinstance(stig_set, StigamataSet):
            raise ValueError("__stig_set__ cannot be None")
        stig_name = stig_set.name
        stig_pos = int(stig_pos)
        
        if stig_pos == 0:
            interested_dict = cls.t_piece
        elif stig_pos == 1:
            interested_dict = cls.m_piece
        else:
            interested_dict = cls.b_piece

        if stig_name not in interested_dict:
            interested_dict[stig_name] = super().__call__(*args, **kwargs)
        
        return interested_dict[stig_name]


@dataclass
class StigamataPiece(metaclass=StigPieceMetaClass):
    __stig_pos__ : int
    __stig_set__ : 'StigamataSet'

    def __post_init__(self):
        if not (0 <= self.__stig_pos__ <=2):
            raise ValueError("__stig_pos__ must be between 0 and 2")

    @property
    def is_top(self):
        return self.__stig_pos__ == 0

    @property
    def is_middle(self):
        return self.__stig_pos__ == 1

    @property
    def is_bottom(self):
        return self.__stig_pos__ == 2

    @staticmethod
    def get_top(stig_name : str):
        return StigamataPiece.t_piece.get(stig_name, None)
    
    @staticmethod
    def get_middle(stig_name : str):
        return StigamataPiece.m_piece.get(stig_name, None)

    @staticmethod
    def get_bottom(stig_name : str):
        return StigamataPiece.b_piece.get(stig_name, None)
    
    @property
    def effect(self):
        return self.__stig_set__.effect(self.__stig_pos__)

    @property
    def hoyo_id(self):
        return self.__stig_set__.__lab_ids__[self.__stig_pos__]

    def __str__(self) -> str:
        if self.is_top:
            return f"{self.__stig_set__.__set_name__} (T)"
        elif self.is_middle:
            return f"{self.__stig_set__.__set_name__} (M)"
        else:
            return f"{self.__stig_set__.__set_name__} (B)"


class StigmataSetMetaClass(type):
    instances = {}
    alt_name_instances = {}

    def __call__(cls, *args, **kwargs):
        if "__set_name__" not in kwargs:
            raise ValueError("__set_name__ is required")
        set_name = kwargs.get("__set_name__", None)
        if set_name is None:
            raise ValueError("__set_name__ cannot be None")

        if set_name not in cls.instances:
            make_item = super().__call__(*args, **kwargs)

            if "alt_name" in kwargs:
                alt_name = kwargs.pop("alt_name", None)
                if alt_name is not None and isinstance(alt_name, typing.List[str]):
                    for name in alt_name:
                        cls.alt_name_instances[name] = cls.instances[set_name]

                else:
                    raise ValueError("alt_name must be a list of string")
            
            cls.instances[set_name] = make_item

        return cls.instances[set_name]

@dataclass
class StigamataSet(metaclass=StigmataSetMetaClass):
    __set_name__ : str
    __top_e__ : str = None
    __mid_e__ : str = None
    __bot_e__ : str = None
    __two_piece__ : str = None
    __three_piece__ : str = None
    __lab_id__ : int = None
    __lab_ids__ : typing.List[int] = [None, None, None]
    __else__ : dict = {}

    def __post_init__(self):
        top = self.top
        mid = self.middle
        bot = self.bottom

    @property
    def name(self):
        return self.__set_name__

    def effect(self, pos: int):
        if pos == 0:
            return self.__top_e__
        elif pos == 1:
            return self.__mid_e__
        elif pos == 2:
            return self.__bot_e__
        else:
            raise ValueError("pos must be between 0 and 2")

    def has_effect(self, pos: int):
        return self.effect(pos) is not None

    @property
    def has_top(self):
        return self.__top_e__ is not None

    @property
    def has_middle(self):
        return self.__mid_e__ is not None
    
    @property
    def has_bottom(self):
        return self.__bot_e__ is not None

    @property
    def top(self):
        if not self.has_top:
            return None

        return StigamataPiece(
            __stig_pos__=0,
            __stig_set__=self
        )

    @property
    def middle(self):
        if not self.has_middle:
            return None

        return StigamataPiece(
            __stig_pos__=1,
            __stig_set__=self
        )
    
    @property
    def bottom(self):
        if not self.has_bottom:
            return None
    
        return StigamataPiece(
            __stig_pos__=2,
            __stig_set__=self
        )

    @property
    def two_piece(self) -> str:
        return self.__two_piece__
    
    @property
    def three_piece(self) -> str:
        return self.__three_piece__

    @staticmethod
    def create(
        name : str, 
        top : str = None, 
        mid : str = None, 
        bot : str = None, 
        two_piece : str = None, 
        three_piece : str = None,
        top_id : int = None,
        mid_id : int = None,
        bot_id : int = None,
        id : int = None,
        alternative_names : typing.List[str] = None,
        **kwargs
    ):
        return StigamataSet(
            __set_name__=name,
            __top_e__=top,
            __mid_e__=mid,
            __bot_e__=bot,
            __two_piece__=two_piece,
            __three_piece__=three_piece,
            __lab_id__=id,
            __lab_ids__=[top_id, mid_id, bot_id],
            alt_names = alternative_names,
            __else__=kwargs
        )

    @staticmethod
    def get(name : str, alt : bool = False):
        if alt and name in StigmataSetMetaClass.alt_name_instances:
            return StigmataSetMetaClass.alt_name_instances[name]

        return StigmataSetMetaClass.instances.get(name, None)
        