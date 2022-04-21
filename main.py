import logging
import sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

import honkaiDex.profile.cached
from honkaiDex import StigamataSet

Allan_Poe_t = StigamataSet.get("allan poe").top
print(Allan_Poe_t)
print(Allan_Poe_t.effect)



