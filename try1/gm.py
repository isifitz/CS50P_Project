import json

def main():
    grocery = load_json()
    make_glist(grocery)

def load_json():
    # migh need to add something to check if file exists
    with open("example.json", "r") as f:
        groceries = json.load(f)
    return groceries

def update_json(grocery):
    with open("grocery2.json", "w", encoding="utf-8") as updated_file:
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

if __name__ == "__main__":
    main()