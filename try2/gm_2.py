import json
import os
import sys
from tabulate import tabulate

def main():
    grocery = load_json()
    update_with_shopping_list(grocery)

def load_json():
    # migh need to add something to check if file exists
    with open("example_2.json", "r") as f:
        groceries = json.load(f)
    return groceries

def update_json(grocery):
    with open("grocery2_2.json", "w", encoding="utf-8") as updated_file:
        json.dump(grocery, updated_file, indent=2)

def input_int(message):
    return int(input(message))

def add_item(grocery):
    item = input("Item name: ")
    amount = input_int("Amount: ")
    threshold = input_int("Threshold for refreshing: ")
    grocery.append({item:{'quantity':amount,'threshold':threshold}}, grocery)
    update_json(grocery)
    return grocery

def add_amount(grocery:dict, args:list=[True]):
    print(args)
    if args[0] is True:
        item = input('Which item would you like to add to: ')
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        amount = input_int("how much would you like to add: ")
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        print(f"Add amounts: {item} +{amount}")

    grocery[item]["quantity"] += amount
    update_json(grocery)
    return grocery

def remove_amount(grocery:dict, args:list=[True]):
    if args[0] is True:
        item = input('Which item would you like to update: ')
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        amount = input_int("how much would you like to remove: ")
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        print(f"Add amounts: {item} +{amount}")
        
    grocery[item]["quantity"] -= amount
    if grocery[item]["quantity"] < 0:
        grocery[item]["quantity"] = 0
    update_json(grocery)
    return grocery

def make_glist(grocery:dict):
    grocery_list = []
    for x,item in grocery.items():
        if item["quantity"] <= item["threshold"]:
            grocery_list.append(x)
    if grocery_list == []:
        print("you good mud")
    else:
        print("Heres your grocery list:")
        with open("grocery_list.txt", "w") as f:
            for x in grocery_list:
                print(x)
                f.write(x + '\n')

def hard_set_amounts(grocery:dict, args:list=[True]):
    if args[0] is True:
        item = input('Which item would you like to set amounts for: ')
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        amount = input_int("What amount do you want to set it to: ")
    else:
        item = args[0]
        amount = int(args[1])
        if item not in grocery.keys():
            sys.exit(f"{item} is not in json.")
        print(f"Set amount: {item} +{amount}")
    
    grocery[item]["quantity"] = amount
    update_json(grocery)
    return grocery

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
        return grocery
    else:
        print("No shopping list found")

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

if __name__ == "__main__":
    main()
