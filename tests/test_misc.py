import unittest
from honkaiDex.base.character import CharacterTag
from honkaiDex.config import config, gconfig, has_gconfig
class misc_test(unittest.TestCase):

    def test_character_tag_get(self):
        print(CharacterTag.get("burst").name)


    def test_cls_in_cls(self):
        print(config.profile.cached.STIGAMATA)
        gconfig.STIGAMATA = "stigamata_2"
        self.assertTrue(has_gconfig(config.profile.cached, "STIGAMATA"))
        print(config.profile.cached.STIGAMATA)
        config.profile.cached.STIGAMATA = "stigamata_3"
        self.assertFalse(has_gconfig(config.profile.cached, "STIGAMATA"))
        print(gconfig.STIGAMATA)