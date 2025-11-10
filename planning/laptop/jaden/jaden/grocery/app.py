import grocery as G
import json

'''
items = [{"name" : "chicken" , "quantity" : 3, "threshold" : 2},
             {"name" : "milk" ,"quantity" : 6, "threshold" : 2},
             {"name" : "eggs" ,"quantity" : 30, "threshold" : 12}]
'''

def main():
    items = [{"name" : "chicken" , "quantity" : 3, "threshold" : 2},
             {"name" : "milk" ,"quantity" : 6, "threshold" : 2},
             {"name" : "eggs" ,"quantity" : 30, "threshold" : 12}]
    initialize_fridge_list(items)


def new_fridge_item():
    name = input("Name of item: ")
    amount = int(input("Current Amount: "))
    threshold = int(input("Buy more threshold: "))
    item = {"name": name, "amount": amount, "threshold": threshold}
    return item


def initialize_fridge_list(items):
    fri_list = json.dumps(items, indent=4, separators=(". ", " = "))
    print(fri_list)
    with open("fridge.json", "w", encoding='utf-8') as file:
        json.dump(items, file, indent=4)


def initialise_fridge_json(grocery_list):
    ...


if __name__ == "__main__":
    main()
