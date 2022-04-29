import honkaiDex.profile.just_character
from honkaiDex import BaseCharacter, Battlesuit
import unittest

class t_full_cycle(unittest.TestCase):
    def test_create_battlesuit(self):
        kiana = BaseCharacter.fuzzy_match_names("kiana")[0][0]
        
        god_kiana = Battlesuit.create(
            name="god kiana", 
            base_character=kiana,
            type="IMG",
            version_released="999.999",
            rarity="S",
            tags=["god", "kiana"],
            nickname = ["god kiana"],
        )
        print(god_kiana)
        self.assertEqual(god_kiana.name, "god kiana")

class t_search(unittest.TestCase):
    def test_battlesuit_name_partial(self):
        item  = Battlesuit.fuzzy_match_names(name="white")[0][0]
        self.assertEqual(item.name, "White Comet")

        item = Battlesuit.fuzzy_match_names(name=" Eclipse")[0][0]
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

        item = Battlesuit.fuzzy_match_names(name="Vermilion Knight - Eclipse")[0][0]
        self.assertEqual(item.name, "Vermilion Knight - Eclipse")

        item = Battlesuit.fuzzy_match_names(name="Starlit Astrologos")[0][0]
        self.assertEqual(item.name, "Starlit Astrologos")