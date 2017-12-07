import random
import time
class orcs:
    orc_basic={"hp":25, "weapon":(darts,knife)}
    orc_archer={"hp":15, "weapon":(darts,bow)}
    def make_enemie(caste, number):
        for b in range(0,number):
            if caste=="basic":
                new_bot={}
                new_bot="orc_bot_"+str(n)+"={}"
                eval(new_bot)
                "=orc_basic+
