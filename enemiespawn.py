import random
import time
import pythonrpg
class orcs:
    orc_basic={"hp":25, "weapon":(random.choice([pythonrpg.items.darts,pythonrpg.items.knife]))}
    orc_archer={"hp":15, "weapon":(random.choice([pythonrpg.items.darts,pythonrpg.items.bow]))}
    def make_enemie(caste, number):
        for b in range(0,number):
            if caste=="basic":
                new_bot={}
                eval("orc_bot_"+str(n)+"={}")
