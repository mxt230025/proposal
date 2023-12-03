import csv
import random
import os
from moviepy.editor import *
import pygame


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
        print("Your inventory is empty. Pull for some items!")


def rare_pity(filename):
    # Items in tiers
    rare_items = ["Gale Gauntlet", "Stave of the Stars", "Sacred Sword", "Fast Past Rapier", "Giants Toothpick"]
    # Pick an item from tiers
    rare_tier = random.choice(rare_items)
    # Pick rare tier
    random_tier = [rare_tier]
    # Remove [ ] '
    original_message=str(random_tier)
    remove_apostrophe=original_message.replace("'","")
    remove_bracket=remove_apostrophe.replace("[","")
    new_message=remove_bracket.replace("]","")
    # Identify rare rarity
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
    legendary_items = ["Tsunami Spear", "Hellfire Hammer", "Absolute Armor", "Eye of the Oracle", "The Stick"]
    # Pick an item from tiers
    legendary_tier = random.choice(legendary_items)
    # Pick legendary tier
    random_tier = [legendary_tier]
    # Remove [ ] '
    original_message=str(random_tier)
    remove_apostrophe=original_message.replace("'","")
    remove_bracket=remove_apostrophe.replace("[","")
    new_message=remove_bracket.replace("]","")
    # Identify legendary rarity
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
    common_items = ["Blunt Sword", "Rusty Hatchet", "Antique Bow", "Worn Shield", "Dull Dagger", "Dusty Scroll", "The Big Stick"]
    rare_items = ["Gale Gauntlet", "Stave of the Stars", "Sacred Sword", "Fast Past Rapier", "Giants Toothpick"]
    legendary_items = ["Tsunami Spear", "Hellfire Hammer", "Absolute Armor", "Eye of the Oracle", "The Stick"]
    # Pick an item from tiers
    common_tier = random.choice(common_items)
    rare_tier = random.choice(rare_items)
    legendary_tier = random.choice(legendary_items)
    # Pick a random tier
    random_tier = [common_tier, rare_tier, legendary_tier]
    random_item = random.choices(random_tier, weights=(90, 20, 1))
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
    pygame.display.set_caption('Welcome to the Game')
    clip = VideoFileClip('intro_animation.mp4')
    clip.preview()
    pygame.quit()
    print()  # Blank line for cleanliness
    print("Welcome to the PFDA Gacha Game!")
    print("I will guarantee that you get a rare item within 10 pulls" +
          " and a legendary item within 100 pulls.")
    filename = 'inventory.csv'
    rare_count = 0
    legendary_count = 0
    anim_toggle = "on"
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
        print("Your inventory is empty. Pull for some items!")
    prompt_msg = ("Enter 'd' / 'display' to display items, 'p' / 'pull' to " +
                  "pull for items, 'c' / or 'clear' to clear inventory, " +
                  "'t' / 'toggle' to toggle animation, or 'q' / 'quit' to quit: ")
    if anim_toggle == "on":
        print("Animations are currently enabled.")
    elif anim_toggle == "off":
        print("Animations are currently disabled.")
    while True:
        print()  # Blank line for cleanliness
        choice = input(f"{prompt_msg}").lower()
        if choice == "d" or choice == "display": # Open inventory
            display_inventory(filename)
        elif choice == "p" or choice == "pull": # Pull for items
            pull_amount = int(input("Would you like to do '1', '5', or '10' pulls? "))
            if pull_amount == 1 or pull_amount == 5 or pull_amount == 10: # Pull X amount of times
                if anim_toggle == "on":
                    pygame.display.set_caption('Pulling for Item...')
                    clip = VideoFileClip('pull_animation.mp4')
                    clip.preview()
                    pygame.quit()
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
        elif choice == "c" or choice == "clear": # Clear inventory
            if(os.path.exists(filename) and os.path.isfile(filename)): 
                os.remove(filename) 
                print("Your inventory has been cleared.")
            else: 
                print("Your inventory is empty. Pull for some items!")
        elif choice == "t" or choice == "toggle": # Toggle animation
            if anim_toggle == "on":
                anim_toggle = "off"
                print("Animations have been disabled.")
            elif anim_toggle == "off":
                anim_toggle = "on"
                print("Animations have been enabled.")
        elif choice == "q" or choice == "quit": # Quit program
            break
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()