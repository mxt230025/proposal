import random

#items in tiers
common_items = ['wood sword', 'wood axe', 'wood spear', 'wood shield', 'wood bow']
rare_items = ['iron sword', 'iron axe', 'iron spear', 'iron shield', 'iron bow']
epic_items = ['diamond sword', 'diamond axe', 'diamond spear', 'diamond shield', 'diamond bow']

#pick a random item from list
common_tier = random.choices(common_items)
rare_tier = random.choices(rare_items)
epic_tier = random.choices(epic_items)

#pick a tier
tiers = [common_tier,rare_tier,epic_tier]
chance = [50,25,25]

#pick a random tier based on chance
random_item = random.choices(tiers)
original_message=str(random_item)
remove_left_bracket=original_message.replace("[","")
remove_right_bracket=remove_left_bracket.replace("]","")
new_message=remove_right_bracket.replace("'","")
print(random_item)
print(new_message)
check = new_message in common_items
print(check)