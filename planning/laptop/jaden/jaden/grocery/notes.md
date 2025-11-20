## TODO
- [ ] initialize json file
- [ ] write to json file
- [ ] create a item
- [ ] add a item to list
- [ ] init the list from json
- [ ] figure out lists
- [ ] 
- [ ] 
- [ ] 
- [ ] 

## notes to me
all things to do with init should use "w" whereas loading should use "r" and adding should use "a"
Then also for 


## Rest of the stuff

So lets think

first thing that I'd need is the json file stuff


format
```json
{
    "fridge" : [
        {"name" : "chicken" ,
        "quantity" : 3,
        "threshold" : 2},
        {"name" : "milk",
        "quantity" : 6,
        "threshold" : 2},
        {"name" : "eggs" ,
        "quantity" : 30,
        "threshold" : 12}
    ]
}
```

roughly something like that
so next step would be to set up code for initializing the file and just loading the file and list.

fridge is what you have
g list is what you need to buy

so we just want to make a fridge item

## The JSON file
This file holds all the house items.
has categories for where the food is:
Fridge, cupboard and freezer (eg.)
then each of them contain the things they have
fridge has fridge things
cupboard has spice and onions, etc.
freezer has meat, etc.
reason for this is things like things that go bad etc.

bathroom, cleaning, etc. for more things in this regard

simplify for now just fridge

file needs a name like "house_inventory" or some shi

## In program itself
you have all the separate things as there own thing
so fridge_list, panty_list, cleaning_list, etc.
They have their own unique things like fridge is when it's old, freezer use by or some shi like that
Have a "added it date" and things in that regard

