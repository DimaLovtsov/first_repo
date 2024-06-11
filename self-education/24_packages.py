#Create a package Dota 2 (Main) which contains packages Characters, Creeps, Items, Runes
#In Characters create AA, Warlock, Techies
#In Creeps create lane_creeps, neutral_creeps
#In Items create ward, clarity, tango, tp
#In Runs create bounty_rune, wisdome_rune


# import Dota2.Items.clarity

# Dota2.Items.clarity.clarity_info()

# from Dota2.Items import tango

# tango.tango_info()


import Dota2.Characters.AA

Dota2.Characters.AA.aspect() #You have taken Ansient Apparition

from Dota2.Characters import Warlock

Warlock.aspect() #You have taken Warlock

from Dota2.Characters.Techies import aspect

aspect() #You have taken Techies


from Dota2.Basics_Items import clarity, tango, ward

clarity.clarity_info()
tango.tango_info()
ward.ward_info()








