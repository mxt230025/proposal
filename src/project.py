import csv
import random

def display_inventory(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                if len(line)==2:
                    tier, original_item=line
                    remove_apostrophe=original_item.replace("'","")
                    remove_bracket=remove_apostrophe.replace("[","")
                    edited_item=remove_bracket.replace("]","")
                    print(f"{edited_item} - {tier} Tier")
    except FileNotFoundError:
        print("Invalid input. Please try again")

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
    random_item = random.choices(random_tier, weights=(90, 10, 1))
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
                    pull_item(filename)
                    counter += 1
            else:
                print("Invalid input. Please try again")
        elif choice == "q" or choice == "quit": # Quit program
            break
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()