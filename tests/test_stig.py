import logging
from pprint import pprint
import honkaiDex.profile.just_stigamata
from honkaiDex import StigamataSet
import unittest
import sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

class t_stig(unittest.TestCase):
    def test_stig_soemthing(self):
        res : StigamataSet =StigamataSet.get_from_name(
            name="zhenyi",partial=True
        )
        
        print(res.top.effect)
        print("?")
        print(res.middle.effect)
        print("?")
        print(res.bottom.effect)