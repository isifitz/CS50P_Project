import gm_2 as G
import argparse

def main():
    grocery = G.load_json()
    parser_func(grocery)

def parser_func(grocery:dict):
    parser = argparse.ArgumentParser(description="Grocey manager.")

    parser.add_argument(
        "-n",
        "--new_item",
        action="store_true",
        help="Interactively add a new item to the inventory."
    )
    parser.add_argument(
        "-a",
        "--add_amount",
        action="store_true",
        help="Interactively increase the quantity of an existing item."
    )
    parser.add_argument(
        "-r",
        "--reduce_amount",
        action="store_true",
        help="Interactively reduce the quantity of an existing item."
    )
    parser.add_argument(
        "-s",
        "--set_amount",
        action="store_true",
        help="Interactively set the quantity of an existing item."
    )
    parser.add_argument(
        "-gl", "--make_grocery_list",
        action="store_true",
        help="Generate grocery_list.txt based on items that are running low."
        )
    parser.add_argument(
        "-sl", "--use_shopping_list",
        action="store_true",
        help="Update inventory using shopping.csv"
        )

    args = parser.parse_args()
    dispatch_actions(args, grocery)

def launch_tui(grocery:dict):
    print("Would have launched tui")
    
def dispatch_actions(args, grocery:dict):
    """Handle the actions requested on the command line."""

    if args.make_grocery_list:
        G.make_glist(grocery)
    elif args.use_shopping_list:
        G.update_with_shopping_list(grocery)
    elif args.new_item:
        G.add_item(grocery)
    elif args.add_amount:
        G.add_amount(grocery)
    elif args.reduce_amount:
        G.remove_amount(grocery)
    elif args.set_amount:
        G.hard_set_amounts(grocery)
    else:
        launch_tui(grocery) # DUH


if __name__ == "__main__":
    main()
