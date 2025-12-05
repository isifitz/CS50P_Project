from fridge.grocery import update_json
from tabulate import tabulate
import os

# still need to validate the input here
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
        return grocery
    else:
        print("No shopping list found")

