import gm_2 as G
import argparse

def main():
    grocery = G.load_json()
    parser_func(grocery)

def parser_func(grocery:dict):
    parser = argparse.ArgumentParser(description="Grocey manager.")

    parser.add_argument("-n", "--new_item", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-a", "--add_amount", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-r", "--reduce_amount", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-s", "--set_amount", nargs=2, metavar=("NAME", "AMOUNT"))
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
    """Handle the actions requested on the command line.

    For now this only wires up the \"make grocery list\" flag.
    You can extend this with more `if` blocks for the other
    arguments (new item, add amount, etc.).
    """

    if args.make_grocery_list:
        G.make_glist(grocery)
    elif args.use_shopping_list:
        G.update_with_shopping_list(grocery)
        # then elif the rest 
    # elif args.add_amount ...
    else:
        launch_tui(grocery) # DUH


if __name__ == "__main__":
    main()