import gm_2 as G
import argparse

def main():
    grocery = G.load_json()
    parser_func(grocery)

def parser_func(grocery:dict):
    parser = argparse.ArgumentParser(description="Grocey manager.")

    parser.add_argument(
        "-a",
        "--add_amount",
        nargs='*',
        default=False,
        help="Add stock to an existing item."
    )
    parser.add_argument(
        "-r",
        "--reduce_amount",
        nargs='*',
        default=False,
        help="Interactively reduce the quantity of an existing item."
    )
    parser.add_argument(
        "-s",
        "--set_amount",
        nargs='*',
        default=False,
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
    parser.add_argument(
        "-n",
        "--new_item",
        action="store_true",
        help="Interactively add a new item to the inventory."
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
    elif type(args.add_amount) is list:
        if len(args.add_amount) != 2:
            args.add_amount.append(True)
        G.add_amount(grocery,args.add_amount)
    elif type(args.reduce_amount) is list:
        if len(args.reduce_amount) != 2:
            args.reduce_amount.append(True)
        G.remove_amount(grocery,args.reduce_amount)
    elif type(args.set_amount) is list:
        if len(args.set_amount) != 2:
            args.set_amount.append(True)
        G.remove_amount(grocery,args.set_amount)
    elif type(args.set_amount) is list:
        if len(args.set_amount) != 2:
            args.set_amount.append(True)
        G.remove_amount(grocery,args.set_amount)
    else:
        launch_tui(grocery)


if __name__ == "__main__":
    main()
