import grocery as g

def main():
    inventory = load_inventory()
    view_inventory(inventory)

def init_inventory():
    ...

def load_inventory() -> dict:
    return g.load_inventory()

def view_inventory(inv_variable:dict): 
    print(inv_variable)

if __name__ == "__main__":
    main()