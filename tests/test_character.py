import honkaiDex.profile.just_character
from honkaiDex import BaseCharacter, Battlesuit
import unittest

class t_full_cycle(unittest.TestCase):
    def test_create_battlesuit(self):
        kiana = BaseCharacter.get_from_name("kiana", partial=True)
        
        god_kiana = Battlesuit.create(
            name="god kiana", 
            base_character=kiana,
            type="IMG",
            version_released="999.999",
            rarity="S",
            tags=["god", "kiana"],
            nickname = ["god kiana"],
        )

        self.assertEqual(god_kiana.name, "god kiana")

class t_search(unittest.TestCase):
    def test_battlesuit_name_partial(self):
        item  = Battlesuit.get_from_name(name="hite", partial=True)
        self.assertEqual(item.name, "White Comet")

        item = Battlesuit.get_from_name(name=" Eclipse", partial=True)
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

        item = Battlesuit.get_from_name(name="Vermilion Knight - Eclipse", partial=True)
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

        item = Battlesuit.get_from_name(name="Starlit Astrologos", partial=True)
        self.assertEqual(item.name, "Starlit Astrologos")