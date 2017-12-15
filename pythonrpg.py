import os
import math
import keyboard
###############################
player_data={"name":"", "gender":"", 'max_hp':100, 'hp':100, 'max_mp':20, "mp":20, "xp":0, "max_inv":20, "inv":20, "gold":0}
data=open('data.txt','w')
locations={"home":0, "base":1,}
weapons=[]
inventory=[]
items={}
loc=""
##################################
def ask1():
    print("load or new?")
    global choice_1
    choice_1=input()
    if choice_1=="load":
        dr=open('data.txt', 'r')
        dr.readline(1)
        dr.readline(2)
        dr.readline(3)
        dr.readline(4)
        dr.readline(5)
        dr.readline(6)
        dr.close()
######################################
    else:
            print("lets get you started!")
            print("name")
            new_name=input()
            print("gender")
            new_gender=input()
            loc="home"
            new_player_data={"name":new_name, "gender":new_gender}
            player_data.update(new_player_data)
            data.truncate()
########################################
def save_game():
    data.write("player_data="+str(player_data)+"\n"+"locations="+str(locations)+"\n"+"weapons="+str(weapons)+"\n"+"inventory="+str(inventory)+"\n"+"items="+str(items)+"\n"+"loc="+str(loc))
#######################################
def battle_choices(condition):
	if condition==0:
		print("spell, attack, item, skip, run")
		bc1=input()
		if bc1=="spell":
			print("these are your spells:", spells)
			spell_choice=input()
			spell_to_cast="spell_cast_"+spell_choice+"()"
			eval(spell_to_cast)
		elif bcl=="attack":
			print("these are your equipped weapons:", weapons)
			attack_choice=input()
			attack_to_cast="attack_cast_"+attack_choice+"()"
			eval(attack_to_cast)
		elif bc1=="item":
			print("these are your current items:", items)
			item_choice=input()
			item_to_cast="item_cast_"+item_choice+"()"
			eval(item_to_cast)
		elif bc1=="skip":
			skip_turn()
		elif bc1=="run":
			attemt_run()
		else:
			print("invalid choice!")
			battle_choices(0)
#################################################
class items:
	knife={"weight":0.5, "damage":"1d4", "type":"physical/slash", "description":"a small knife. not very strong, but good enough in a fight"}
	walking_stick={"weight":0,  "damage":"1d4", "type":"magic/general", "description":"a walking stick marked with runes. a basic mage weapon."}
	darts={"weight":0.2, "damage":"1d4", "type":"physical/pen", "description":"throwing darts. must be retrieved."}
	bow={"weight":1, "damage":"1d8", "type":"physical/pen", "description":"a simple yew bow. needs arrows, though"}

################################################
class MainLoop():
    def on_load_intro(condition):
        if condition==0:
            print("it is late at night, the stars are out, and you are sound asleep")
            print("you wake suddenly, your lungs burn and an acrid smell fills your nose.")
            print("everything seems hazy and there is an eerie glow around your room.")
            print("then, it hits you. your house is on fire. you have mere seconds to get out, and as you run through")
            print("your hall, you remember the gear in your closet. you quickly grab a pack, a few clothes, ")
            print("but you only have time to get one weapon, a rusty dagger, a work out walking stick,")
            print("some dull throwing darts, or a creaky old bow.")
            print("knife, stick, darts, or bow?")
            go=True
            while go:
                intro_choice_1=input()
                if intro_choice_1=="knife":
                    weapons.append(knife)
                    inventory.append(knife)
                    go=False
                elif intro_choice_1=="stick":
                    weapons.append(walking_stick)
                    inventory.append(walking_stick)
                    go=False
                elif intro_choice_1=="darts":
                    weapons.append(darts)
                    inventory.append(darts)
                    go=False
                elif intro_choice_1=="bow":
                    weapons.append(bow)
                    inventory.append(bow)
                    go=False
                else:
                    print("i cannot do this. maybe something else")
                    go=True
                
save_game()
data.close()
