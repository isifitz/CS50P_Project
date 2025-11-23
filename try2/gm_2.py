import json
import os

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

def add_amount(grocery:dict):
    item = input('Which item would you like to add to: ')
    if item not in grocery.keys():
        print("not in json. add this")
    else:
        amount = input_int("how much would you like to add: ")
        grocery[item]["quantity"] += amount
        update_json(grocery)
    return grocery

def remove_amount(grocery:dict):
    item = input('Which item would you like to update: ')
    if item not in grocery.keys():
        print("not in json. add this")
    else:
        amount = input_int("how much would you like to remove: ")
        grocery[item]["quantity"] -= amount
        if grocery[item]["quantity"] < 0:
            grocery[item]["quantity"] = 0
        update_json(grocery)
    return grocery
    # ideal way this would work is you give a list of what you used instead of one by one

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

def hard_set_amounts(grocery:dict):
    item = input('Which item would you like to set amounts for: ')
    if item not in grocery.keys():
        print("not in json. add this")
    else:
        amount = input_int("What amount do you want to set it to: ")
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

def arg_system(grocery:dict):
    ...
    # so first it checks if there any args

    # then if there are args and does "tool calling"


if __name__ == "__main__":
    main()
