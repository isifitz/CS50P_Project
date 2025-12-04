import inquirer
from tabulate import tabulate
import gm_2 as G

def main():
    test_tabulate()

def test_inquirer():
    unit = inquirer.list_input("Metric or Imperial", choices=['Metric', 'Imperial'])
    print(unit)
    '''questions = [
        inquirer.Text("user", message="Please enter your github username", validate=lambda _, x: x != "."),
        inquirer.Password("password", message="Please enter your password"),
        inquirer.Text("repo", message="Please enter the repo name", default="default"),
        inquirer.Checkbox(
            "topics",
            message="Please define your type of project?",
            choices=["common", "backend", "frontend"],
        ),
        inquirer.Text(
            "organization",
            message=(
                "If this is a repo from a organization please enter the organization name,"
                " if not just leave this blank"
            ),
        ),
        inquirer.Confirm(
            "correct",
            message="This will delete all your current labels and create a new ones. Continue?",
            default=False,
        ),
    ]

    answers = inquirer.prompt(questions)
    print(answers)'''

def test_tabulate():
    data = [
        ["Alice", 24, "Engineer"],
        ["Bob", 30, "Data Scientist"],
        ["Charlie", 28, "Teacher"]
    ]

    table = tabulate(data, headers=["Name", "Age", "Profession"], tablefmt="grid")

    print(table)

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
        show_stock_table(grocery)
    else: 
        print("Quitting")

def show_stock_table(grocery:dict):
    data = []
    counter = 0
    for groc in grocery.items():
        item = groc[0]
        value = groc[1]['quantity']
        threshold = groc[1]['threshold']
        data.append([item,value,threshold])
        counter += 1
    table = tabulate(data,headers=["Items","Amount","Threshold"],tablefmt="double_outline")
    print(table)

if __name__ == "__main__":
    dispatch_actions(func_inquirer())