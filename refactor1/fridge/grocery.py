import json
import os
import sys
import inquirer

# this loads up the json file and gives you a dict variable to make changes, 
# every function then calls update_json there after
def load_json() -> dict: 
    with open("fridge.json", "r", encoding="utf-8") as f:
        groceries = json.load(f)
    print("Successfully loaded fridge!")
    return groceries

# this always updates the json file whenever changes are made
def update_json(grocery:dict) -> None: # updates a file but idk how to show that
    with open("fridge.json", "w", encoding="utf-8") as updated_file:
        json.dump(grocery, updated_file, indent=2)
    print("Successfully updated fridge!")

# Initialise a fridge if one isn't present
def init_json() -> None: # makes a file but idk how to show that
    if os.path.exists("fridge.json"):
        sys.exit("Fridge file already exists.")
    else:
        grocery = {}
        item = input("Item name: ").lower()
        amount = int(input("Amount: "))
        threshold = int(input("Threshold for refreshing: "))
        grocery.update({item:{'quantity':amount,'threshold':threshold}})
        update_json(grocery)
        print("Fridge file created")

# this is what you run to startup the app and get the grocery dict
# if there is a fridge file it just loads up or you may initialise a new one
def startup() -> dict :
    '''
    Loads the fridge or propmts user to initialise one
    
    :return: The grocery dict object 
    :rtype: dict
    '''
    if os.path.exists("fridge.json"):
        return load_json()
    else:
        message = inquirer.confirm("No fridge file dectected. Would you like to create one")
        if message: # true or false from the inq.confirm
            init_json()
            return load_json()
        else:
            sys.exit("Thanks for using GroceryM")
