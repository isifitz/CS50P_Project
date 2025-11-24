import gm_2 as G
import argparse
import sys

def main():
    grocery = G.load_json()
    parser_func(grocery)

def parser_func(grocery:dict):
    parser = argparse.ArgumentParser(description="Grocey manager.")

    parser.add_argument("-n", "--new_item", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-a", "--add_amount", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-r", "--reduce_amount", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-hs", "--hardset_amount", nargs=2, metavar=("NAME", "AMOUNT"))
    parser.add_argument("-sl", "--use_shopping_list")
    parser.add_argument("-gl", "--make_grocery_list")

    args = parser.parse_args()

    if no_args_given(args):
        launch_tui(grocery)
    else:
        dispatch_actions(args, grocery)

def no_args_given(args):
    return all(getattr(args, field) is None for field in vars(args))

def launch_tui(grocery:dict):
    print("Would have launched tui")

    
def dispatch_actions(args, grocery:dict):
    ...

    


if __name__ == "__main__":
    main()