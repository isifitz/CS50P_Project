import fridge.processes as p
import sys

def parser_func(grocery:dict={}):
    if len(sys.argv) > 1: # so the argparser doesn't just run
        import argparse
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
        parser.add_argument(
            "-t",
            "--stock_table",
            action="store_true",
            help="Print a table to show stock."
        )

        args = parser.parse_args()
        dispatch_actions(args, grocery)

def dispatch_actions(args, grocery:dict):
    """Handle the actions requested on the command line."""

    if args.make_grocery_list is True:
        p.make_glist(grocery)
    elif args.use_shopping_list is True:
        p.update_with_shopping_list(grocery) 
    elif args.new_item is True:
        p.add_item(grocery)
    elif args.stock_table is True:
        p.show_stock_table(grocery)
    elif type(args.add_amount) is list:
        if len(args.add_amount) != 2:
            args.add_amount.append(True)
        p.add_amount_arg(grocery,args.add_amount)
    elif type(args.reduce_amount) is list:
        if len(args.reduce_amount) != 2:
            args.reduce_amount.append(True)
        p.remove_amount_arg(grocery,args.reduce_amount)
    elif type(args.set_amount) is list:
        if len(args.set_amount) != 2:
            args.set_amount.append(True)
        p.hard_set_amounts_arg(grocery,args.set_amount)
