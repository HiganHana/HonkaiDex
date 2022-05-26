import logging
from pprint import pprint
import sys
import unittest
from hondex_arch import BaseDataclass, baseDataclassMeta
import hondex_arch
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

@unittest.skip("skipping")
class t_base(unittest.TestCase):
    def test_run_stig_scrap(self):
        from hondex_scrap.stigScrapper import StigScrapper

        s = StigScrapper()

        s.run_job(interval=0.5)

    def test_run_char_scrap(self):
        from hondex_scrap.charScrapper import CharScrapper 
        s = CharScrapper()
        s.run_job(interval=0.5)

    def test_run_bs_scrap(self):
        from hondex_scrap.bsScrapper import BSScrapper 
        s = BSScrapper()
        s.run_job(interval=0.5)
        
    def test_1(self):
        from hondex import load_all
        load_all()
        print()

class t_basedataclass(unittest.TestCase):
    def test_init_basedataclass(self):
        x = BaseDataclass(
            name = "test",
            nicknames = ["test3", "test2"],
        )
        self.assertEqual(x.name, "test")
        self.assertEqual(x.nicknames, ("test3", "test2"))

        # check same name 
        with self.assertRaises(ValueError):
            BaseDataclass(
                name = "test",
                nicknames = ["test3", "test2"],
            )

        # check same nickname
        with self.assertRaises(ValueError):
            BaseDataclass(
                name = "test2",
                nicknames = ["test3", "test"],
            )
