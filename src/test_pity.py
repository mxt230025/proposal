import csv
import random
import os

def display_inventory(filename):
    item_number = 1
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if len(line)==2:
                    tier, original_item=line
                    remove_apostrophe=original_item.replace("'","")
                    remove_bracket=remove_apostrophe.replace("[","")
                    edited_item=remove_bracket.replace("]","")
                    print(f"{item_number}. {edited_item} - {tier} Tier")
                    item_number += 1
    except FileNotFoundError:
        print("Invalid input. Please try again")

def rare_pity(filename):
    # Items in tiers
    rare_items = ["Iron Sword", "Iron Axe", "Crossbow"]
    # Pick an item from tiers
    rare_tier = random.choice(rare_items)
    # Pick a random tier
    random_tier = [rare_tier]
    # Remove [ ] '
    original_message=str(random_tier)
    remove_apostrophe=original_message.replace("'","")
    remove_bracket=remove_apostrophe.replace("[","")
    new_message=remove_bracket.replace("]","")
    # Identify item rarity
    if new_message in rare_items:
        rarity = "Rare"
    else:
        rarity = "Null"
    # Add item to inventory, say rarity + new item
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rarity, random.choices(random_tier)])
        print(f"You got a {rarity} {new_message}!")

def legendary_pity(filename):
    # Items in tiers
    legendary_items = ["Diamond Sword", "Diamond Axe", "Spellbook"]
    # Pick an item from tiers
    legendary_tier = random.choice(legendary_items)
    # Pick a random tier
    random_tier = [legendary_tier]
    # Remove [ ] '
    original_message=str(random_tier)
    remove_apostrophe=original_message.replace("'","")
    remove_bracket=remove_apostrophe.replace("[","")
    new_message=remove_bracket.replace("]","")
    # Identify item rarity
    if new_message in legendary_items:
        rarity = "Legendary"
    else:
        rarity = "Null"
    # Add item to inventory, say rarity + new item
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rarity, random.choices(random_tier)])
        print(f"You got a {rarity} {new_message}!")

def pull_item(filename):
    # Items in tiers
    common_items = ["Wood Sword", "Wood Axe", "Wood Bow"]
    rare_items = ["Iron Sword", "Iron Axe", "Crossbow"]
    legendary_items = ["Diamond Sword", "Diamond Axe", "Spellbook"]
    # Pick an item from tiers
    common_tier = random.choice(common_items)
    rare_tier = random.choice(rare_items)
    legendary_tier = random.choice(legendary_items)
    # Pick a random tier
    random_tier = [common_tier, rare_tier, legendary_tier]
    random_item = random.choices(random_tier, weights=(100, 0, 0))
    # Remove [ ] '
    original_message=str(random_item)
    remove_apostrophe=original_message.replace("'","")
    remove_bracket=remove_apostrophe.replace("[","")
    new_message=remove_bracket.replace("]","")
    # Identify item rarity
    if new_message in common_items:
        rarity = "Common"
    elif new_message in rare_items:
        rarity = "Rare"
    elif new_message in legendary_items:
        rarity = "Legendary"
    else:
        rarity = "Null"
    # Add item to inventory, say rarity + new item
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rarity, random.choices(random_item)])
        print(f"You got a {rarity} {new_message}!")

def main():
    print("Welcome to Mason's Gacha Game!")
    filename = 'inventory.csv'

    rare_count = 0
    legendary_count = 0
    # Pity system
    if os.path.exists(filename):
        with open(filename, 'r') as file:
                reader = csv.reader(file)
                for line in reader:
                    if len(line)==2:
                        tier, original_item=line
                        if tier == "Common":
                            rare_count += 1
                            legendary_count += 1
                        if tier == "Rare":
                            rare_count = 0
                            legendary_count += 1
                        if tier == "Legendary":
                            rare_count += 1
                            legendary_count = 0
    else:
        print("Your inventory is empty")

    prompt_msg = ("Enter 'd' / 'display' to display items, 'p' / 'pull' to " +
                  "pull for items, or 'q' / 'quit' to quit: ")
    while True:
        print()  # Blank line for cleanliness
        choice = input(f"{prompt_msg}").lower()
        if choice == "d" or choice == "display": # Open inventory
            display_inventory(filename)
        elif choice == "p" or choice == "pull": # Pull for items
            pull_amount = int(input("Would you like to do '1', '5', or '10' pulls? "))
            if pull_amount == 1 or pull_amount == 5 or pull_amount == 10: # Pull X amount of times
                counter = 0
                while counter < pull_amount:
                    if legendary_count == 99:
                        legendary_pity(filename)
                        counter += 1
                        rare_count = 0
                        legendary_count = 0
                    else:
                        if rare_count == 9:
                            rare_pity(filename)
                            counter += 1
                            rare_count = 0
                            legendary_count += 1
                        else:
                            pull_item(filename)
                            counter += 1
                            rare_count += 1
                            legendary_count += 1
            else:
                print("Please enter '1', '5', or '10' to pull for items.")
        elif choice == "q" or choice == "quit": # Quit program
            break
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()