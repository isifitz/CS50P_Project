import inquirer
from fridge.processes import add_item, hard_set_amounts, add_amount, remove_amount, show_stock_table, make_glist,update_with_shopping_list
import sys

def func_inquirer():
    print()
    run_me = inquirer.list_input(
        "function_name",
        choices=["Add Amount",
                 "Remove Amount",
                 "Make Grocery List",
                 "Hard Set Amount",
                 "Use Shopping List",
                 "Add Item",
                 "Show Stock",
                 "Quit"]
        )
    return run_me

def dispatch_actions(dothis:str,grocery:dict):
    
    if dothis == "Add Item": 
        add_item(grocery)
    elif dothis == "Show Stock":
        show_stock_table(grocery)
    elif dothis == "Make Grocery List":
        make_glist(grocery)
    elif dothis == "Use Shopping List":
        update_with_shopping_list(grocery)
    elif dothis == "Add Amount":
        add_amount(grocery)
    elif dothis == "Remove Amount": 
        remove_amount(grocery)
    elif dothis == "Hard Set Amount": 
        hard_set_amounts(grocery)
    else:
        sys.exit("Thanks for using GroceryM")

def run_tui(grocery:dict):
    dispatch_actions(func_inquirer(),grocery)