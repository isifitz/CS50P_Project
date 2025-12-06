# Just loose thoughts

what else:
the arg system
blame this out quick with sys


- [x] hard setting
- [x] updating json with a shopping list
- [x] using args (this is kind of complicated)
- [ ] now just the TUI (FUH)

## add in remove Item from json

basically the same as new item but remove item from the dictionary then update the json

## Updating with shopping list

so you give a csv file with item and amount and it adds
updating with shopping list needs lots of validation FUH

### Extra notes of shopping list
small test things: should only allow positive amounts

## Arg system

## TODO
- [ ] so get it so it can show a message for each arg case
  - [x] for no args, print would have showed tui
  - [x] g list and shopping list
  - [ ] So the rest

### issue
```
python3 agp_sys.py
    Namespace(new_item=None, add_amount=None, reduce_amount=None, set_amount=None, make_grocery_list=False, use_shopping_list=False)
```

Fuh so now the args aren't empty if you add nothing
so watch a video about using args actually

so if they just use the arg without values then it calls the function but they can also add in the amounts to do it one way

### Adding item
so for adding a item
- you first say you want to
  - Then you can either do it in cl
  - Or just say you want to add item and do it normally

so what arg
-n
--new_item
then item name and amount
eg. -new bread 6 3

### editing amount
-a or -r
--add_amount or --reduce_amount
then item name and amount
eg -a chicken 3 or --reduce_amounts eggs 6

### hard setting amounts
-h
--hardset-amount
eg.

### use shopping list or make grocery list
-sl or -gl
--use-shopping-list or --make-grocery-list
just call the functions





## How this could work

so main mod for calling the app
then have a module for each function that populates the visual part

so imagine it like this:
Grocery_manager
├── main.py
│   ├── this the main thing and have a visual element and the other function just send info or something like that
│   ├── need to figure out how tf to go about this like what style would work best
│   └── specifically built it to work well with django
├── func1
│   └── this could be add or remove
├── func2
│   └── this could ne manage json
└── func3
    └── this could be G list


## AI try

### Arg system

so far it calls the functions perfectly but now we should make it so that you can add in the other info and have it work
**kwargs

I don't know what it means so we need to figure out optional things
so if there is optional stuff it should send the optional stuff

What I need to do
- [ ] make a new file for the implementation of this because it kind of complicated and can break everything
- [ ] first need to allow functions to take in the optional
  - [ ] In my head just do it in agp_sys and refactor later
  - [ ] Lowkey nah because the json
  - [ ] We need to first see what the optional arguments

question:
Ok I want to see what the optional arguments would give so:
These are the ones that need updating, the rest are fine
1. New Item
   1. Item name
   2. Amount you have currently
   3. Threshold for when the item is low (needs to go to shopping list)
2. Add amount
   1. name of item
   2. amount to add
3. Remove amount
   1. name of item
   2. amount to remove
4. Hard set amount
   1. Name
   2. Amount

so the optionals start out as none or is there a better way to go about this
then I need to change the functions in gm_2 for these changes and have it so the agp_sys sends the info IF it is given
The fuh we still need to figure out inquirer and tabulate

so to do is just do 1 of them then follow that
yasis refactoring this gon be hell
then also figuring out a django implementation for this for web and making a swift app for this...

### So current task

Ok so now the add amount is working properly when using args but its now 100%
I am lazy.

this shi complicated af lol
use parse_args for testing

### Codex Plan

1. Inspect the gm_2 helpers and current argparse wiring to confirm what inputs each function expects and how they currently prompt users.
2. Extend the argparse definitions so each action flag optionally accepts the relevant positional arguments (e.g., name/amount/threshold) without breaking the existing interactive mode.
3. Update dispatch_actions to detect whether the optional CLI arguments were supplied; if so, bypass prompts and call the gm_2 helpers with those values, otherwise fall back to the interactive flow.
4. Add guardrails/logging for invalid or incomplete combinations so the user receives guidance when mixing optional CLI inputs with interactive prompts.
# Current work

- [x] Inquirer
  - [x] figure out a ideal flow for the programs tui
  - [x] then make a inquirer for each page
- [x] tabulate
  - [x] this is just for seeing current stock
  - [x] just need to make a new function for seeing current stock and making is view with this

once we finish these 2 then just refactor, clean up and start with testing.
Then make things look nice, get the program cleaned up in one file, start all the requirements for the project (video, etc.) then upload and done

## Inquirer

1. need to go one function at a time
   1. first just add and remove amounts
   2. set amount
   3. add item
   4. 

add amount
remove amount
set amount

add item

make grocery list
use shopping list

## Tabulate

...

## Notes

make diagrams to see where to refactor see the flow and have a low level understanding of the program
so first issue is the whole thing is kind of cooked damn

# Refactor part 1

also use AI after you refac to just go through what you've made and rate it scale of one to 10 and to help with documentation and naming conventions and make everything type safe liinting and allat (also with the script and power point presentation)

and I'll have to refactor to make it work with the project.py and test_project.py for uploading (low key fuhkk)(deadass just put everything on one page lol)

so first need to refact everything into it's own module and figure out how main will call on everything

so first lets start with agp and the stock modules

- [x] groecry.py == main.py
- [ ] 2agp_sys == argp.py
  - [ ] start with add item
- [ ] gm_2.py == processes.py

so what I see is the agp should return run tui or nah
Ok so in dispatch it either returns true or false
so 

## Whats done so far

all the json file related stuff
tui stuff is set up but still needs to be link to the other things

## TODO

so tui and process done
now argp 
dont forget to change the if len in parser_fun
add in

### AGP TODO
- [x] make grocery list
- [x] use shoping list
- [x] new item
- [x] show stock table
- [x] add amount
- [x] reduce amount
- [x] set amount


## Later and extra
### argparser vaildation
argparse in Python does not directly support specifying nargs to accept either 0 or 2 arguments. The nargs argument in argparse.add_argument() allows for specific behaviors:
nargs='?': Allows zero or one argument.
nargs='*': Allows zero or more arguments.
nargs='+': Requires one or more arguments.
nargs=N (an integer): Requires exactly N arguments.
To achieve the effect of accepting either 0 or 2 arguments, a common approach involves a two-step process:
Use nargs='*' or nargs='?' and perform post-parsing validation:
Define the argument with nargs='*' or nargs='?' to allow for a variable number of arguments (including zero).
After parser.parse_args() is called, check the length of the resulting list for that argument.
If the length is not 0 or 2, raise an ArgumentParser.error() to indicate an invalid number of arguments.
Example:
```Python

import argparse

parser = argparse.ArgumentParser(description="Example for 0 or 2 arguments")
parser.add_argument('my_args', nargs='*', help='Provide 0 or 2 arguments')
args = parser.parse_args()

if len(args.my_args) not in [0, 2]:
    parser.error("The 'my_args' argument requires either 0 or 2 values.")

print(f"Received arguments: {args.my_args}")
```

basically in my case
```
if len(args.my_args) n == 0:
  run tui version
if len(args.my_args) n == 2:
  if args.my_args[1] (the number) is int
    run the quick version
  else:
    parser.error("invalid atguments (the second arg must be a int number)")
else:
    parser.error("The 'my_args' argument requires either 0 or 2 values.")
```
