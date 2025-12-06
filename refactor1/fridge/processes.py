from fridge.grocery import update_json
from tabulate import tabulate
import os
import sys

# still need to validate the input here

# This is the TUI section
def add_item(grocery:dict) -> dict:
    '''
    Allow user to add a new item to the fridge if it doesn't exist already.
    
    :param grocery: The object for the current fridge
    :type grocery: dict
    :return: The updated fridge with new item
    :rtype: dict
    '''
    item = input("Item name: ")
    if item in grocery.keys():
        print(f"{item.title()} already in the fridge.")
    else:
        amount = int(input("Amount: "))
        threshold = int(input("Threshold for refreshing: "))
        grocery.update({item:{'quantity':amount,'threshold':threshold}})
        update_json(grocery)
        return grocery

def show_stock_table(grocery:dict):
    data = []
    counter = 0
    for groc in grocery.items():
        item = groc[0]
        value = groc[1]['quantity']
        threshold = groc[1]['threshold']
        data.append([item,value,threshold])
        counter += 1
    table = tabulate(data,headers=["Items","Amount","Threshold"],tablefmt="double_outline")
    print(table)

def make_glist(grocery:dict):
    grocery_list = []
    for x,item in grocery.items():
        if item["quantity"] <= item["threshold"]:
            grocery_list.append(x)
    if grocery_list == []:
        print("You fridge is sufficiently stocked!")
    else:
        print("Heres your grocery list:")
        with open("grocery_list.txt", "w") as f:
            for x in grocery_list:
                print(x)
                f.write(x + '\n')

def update_with_shopping_list(grocery:dict) -> dict | None:
    go = False
    if os.path.exists("shopping.csv"):
        with open("shopping.csv", "r") as f:
            for line in f:
                item , amount = line.split(",")
                if item in grocery.keys():
                    grocery[item]["quantity"] += int(amount)
                    print(f"Added {item}")
                    go = True
                else:
                    print(f"{item} not in json")
        if go:
            update_json(grocery)
            show_stock_table(grocery)
        return grocery
    else:
        print("No shopping list found")

def add_amount(grocery:dict):
    item = input('Which item would you like to add to: ')
    if item not in grocery.keys():
        print(f"{item} is not in the fridge file.")
    else:
        amount = int(input("how much would you like to add: "))
        old_amount = grocery[item]["quantity"]
        grocery[item]["quantity"] += amount
        prt_item_stock(grocery,item,old_amount)
        update_json(grocery)
        return grocery

def remove_amount(grocery:dict):
    item = input('Which item would you like to update: ')
    if item not in grocery.keys():
        print(f"{item} is not in json.")
    else:
        amount = int(input("how much would you like to remove: "))    
        old_amount = grocery[item]["quantity"]
        grocery[item]["quantity"] -= amount
        if grocery[item]["quantity"] < 0:
            grocery[item]["quantity"] = 0
        prt_item_stock(grocery,item,old_amount)
        update_json(grocery)
        return grocery
    
def hard_set_amounts(grocery:dict, args:list=[True]):
    item = input('Which item would you like to set amounts for: ')
    if item not in grocery.keys():
        print(f"{item} is not in json.")
    else:
        amount = int(input("What amount do you want to set it to: "))
        old_amount = grocery[item]["quantity"]
        grocery[item]["quantity"] = amount
        prt_item_stock(grocery,item,old_amount)
        update_json(grocery)
        return grocery

def prt_item_stock(grocery:dict,item:str,old_amount:int):
    print(f"Updated {item} successfully!\n\
  current quantity: {grocery[item]["quantity"]}\n\
  previous quantity: {old_amount}")

# This is the agp section (takes in lists as well)
def add_amount_arg(grocery:dict, args:list):
    # Get the amounts and item name
    if args[0] is True:
        item = input('Which item would you like to add to: ').lower()
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")
        amount = int(input("how much would you like to add: "))
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")

    # make the changes
    old_amount = grocery[item]["quantity"]
    grocery[item]["quantity"] += amount
    prt_item_stock(grocery,item,old_amount)
    update_json(grocery)

def remove_amount_arg(grocery:dict, args:list):
    # Get the amounts and item name
    if args[0] is True:
        item = input('Which item would you like to update: ')
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")
        amount = int(input("how much would you like to remove: "))
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")

    # make the changes
    old_amount = grocery[item]["quantity"]    
    grocery[item]["quantity"] -= amount
    if grocery[item]["quantity"] < 0:
        grocery[item]["quantity"] = 0
    prt_item_stock(grocery,item,old_amount)
    update_json(grocery)

def hard_set_amounts_arg(grocery:dict, args:list):
    # Get the amounts and item name
    if args[0] is True:
        item = input('Which item would you like to set amounts for: ')
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")
        amount = int(input("What amount do you want to set it to: "))
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in the fridge file.")

    # make the changes
    old_amount = grocery[item]["quantity"]
    grocery[item]["quantity"] = amount
    prt_item_stock(grocery,item,old_amount)
    update_json(grocery)
