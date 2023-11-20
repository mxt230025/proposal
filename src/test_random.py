import random

#items in tiers
common_items = ['wood sword', 'wood axe', 'wood spear', 'wood shield', 'wood bow']
rare_items = ['iron sword', 'iron axe', 'iron spear', 'iron shield', 'iron bow']
epic_items = ['diamond sword', 'diamond axe', 'diamond spear', 'diamond shield', 'diamond bow']

#pick a random item from list
common_tier = "COMMON", random.choices(common_items)
rare_tier = "RARE", random.choices(rare_items)
epic_tier = "EPIC", random.choices(epic_items)

#pick a tier
tiers = [common_tier,rare_tier,epic_tier]
chance = [50,25,25]

#pick a random tier based on chance
random_item = random.choices(tiers)
print((random_item))

#selected_item = random.choices(random_tier)
#print((selected_item))