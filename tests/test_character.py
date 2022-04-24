import honkaiDex.profile.just_character
from honkaiDex import BaseCharacter, Battlesuit
import unittest

class t_full_cycle(unittest.TestCase):
    def test_create_battlesuit(self):
        kiana = BaseCharacter.get("kiana", partial_search=True)
        
        god_kiana = Battlesuit.create(
            name="god kiana", 
            base_character=kiana,
            type_="IMG",
            version_released="999.999",
            rarity="S",
            tags=["god", "kiana"],
            abbrevs=[
                "godtuna"
            ]
        )

        self.assertEqual(god_kiana.name, "god kiana")

    


class t_search(unittest.TestCase):
    def test_battlesuit_name_partial(self):
        item  = Battlesuit.get("hite", partial_search=True)
        self.assertEqual(item.name, "White Comet")

        item = Battlesuit.get(" Eclipse", partial_search=True)
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

        item = Battlesuit.get("Vermilion Knight - Eclipse", partial_search=True)
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

    