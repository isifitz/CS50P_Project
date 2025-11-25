# Just loose thoughts

what else:
the arg system
blame this out quick with sys


- [x] hard setting
- [x] updating json with a shopping list
- [ ] using args (this is kind of complicated)
  - [ ] tutorials
  - [ ] implement


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
Just give the AI it's own file with my current code and explain how I want the argparse system to work (as above)

so the way it's finna work
you have the arg system for quick use if you know what you want to do, then a tui if you omit the args
for the tui I want to use a library like use inquirer and tabulate and 

### Arg system

so far it calls the functions perfectly but now we should make it so that you can add in the other info and have it work
**kwargs

I don't know what it means so we need to figure out optional things
so if there is optional stuff it should send the optional stuff

### Codex Plan

1. Inspect the gm_2 helpers and current argparse wiring to confirm what inputs each function expects and how they currently prompt users.
2. Extend the argparse definitions so each action flag optionally accepts the relevant positional arguments (e.g., name/amount/threshold) without breaking the existing interactive mode.
3. Update dispatch_actions to detect whether the optional CLI arguments were supplied; if so, bypass prompts and call the gm_2 helpers with those values, otherwise fall back to the interactive flow.
4. Add guardrails/logging for invalid or incomplete combinations so the user receives guidance when mixing optional CLI inputs with interactive prompts.
