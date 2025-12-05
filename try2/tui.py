import inquirer
import gm_2 as G

def main():
    dispatch_actions(func_inquirer())

def func_inquirer():
    run_me = inquirer.list_input(
        "function_name",
        choices=["Add Amount","Remove Amount","Make Grocery List",
                 "Hard Set Amount","Use Shopping List","Add Item","Show Stock","Quit"]
        )
    return run_me

def dispatch_actions(dothis:str):
    grocery = G.load_json()
    if dothis == "Add Amount":
        G.add_amount(grocery)
    elif dothis == "Remove Amount": 
        G.remove_amount(grocery)
    elif dothis == "Make Grocery List": 
        G.make_glist(grocery)
    elif dothis == "Hard Set Amount": 
        G.hard_set_amounts(grocery)
    elif dothis == "Use Shopping List": 
        G.update_with_shopping_list(grocery)
    elif dothis == "Add Item": 
        G.add_item(grocery)
    elif dothis == "Show Stock": 
        G.show_stock_table(grocery)
    else: 
        print("Quitting")

if __name__ == "__main__":
    main()
