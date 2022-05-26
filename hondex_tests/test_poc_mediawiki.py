from pprint import pprint
import unittest
from mediawiki import MediaWiki

class poc_mediawiki(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        honkai_wiki = MediaWiki(url="https://honkaiimpact3.fandom.com/api.php", rate_limit=True)
        data = honkai_wiki.categorytree(category="Battlesuits", depth=1)
        pprint(data)