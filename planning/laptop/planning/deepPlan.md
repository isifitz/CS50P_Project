# Actual plan for now

## Food
So lets breakdown a chicken
Thats the daily
- 2 breast
- 2 tenderloins
- 2 thighs and drumsticks
- 4 wings

The Macro mince joint
 
2k calories for the day

What do I want to eat
So lets look at it like this.
Eggs
Milk
Spread
yogurt
whey
bread
keep building an essential list with an idea of how to track it.


need to hit about 2.5 cals, 140g proteins, 310g carbs, 70g fats

- chicken
- mince
- steaks (even those minute steaks)(Look into what are cheapest cuts and meal examples)
- eggs
- tuna
- yogurt
- cottage cheese
- whey
- beans
- lentils
(Also for fish break them joints down)

carbs
- rice
- oats
- potatoes
- pasta
- bread
- noodles
- (get in asian bag)
- wraps

fruits
- banana
- blueberries
- oranges
- etc.

vegetables
- beans
- onions
- cabbage
- salad joints
- tomatoes
- etc.

healthy oils
- avo
- nuts
- peanut butter

bonus
- cheese
- honey
- sugar
- herbs, spices, stock

My ideal meal plan
small break (like the egg muffin and coffee, some oats)
small brunch (like a wrap, shake or some)
nice lunch (solid miday meal like a moerse omelette and a coffee)
this is all before 12pm
then another 2 small meals (shakes, noodles)
dinner
night snacks

## RN
so lets sart just with managing a chicken

lets see it with the chicken
this is the first part of the full meal thing

so chicken here
bought a chicken means

```json


Fridge : 
[
{item: Chicken,
amount: ["parts of chicken"],
threshold: "when 2 parts left"}
]
```
so when you cop a chicken it adds all this

how would this code work
```py
'''
first add a chicken
first you say you want to add
you can just select from the list (have categories for cleaning up things or searching)(searching better highkey)
'''
___
def add_item_to_fridge(item,fridge)
    if item == "chicken":
        add_chicken(fridge)

def add_chicken(fridge):
    # works in json
    # add chicken portions to amount of item : chicken
    # fridge[chicken][amount]["breasts"] += 2 
    # fridge[chicken][amount]["drumsticks"] += 2 
    # fridge[chicken][amount]["thighs"] += 2 
    # fridge[chicken][amount]["tenderloins"] += 2 
    # fridge[chicken][amount]["wings"] += 4
___
'''
eat some chicken
ideal way to do this is you say you what to remove
then you say item name then it shows amount so you can be specific
'''
___
def remove_food(item:iterable,amount:int):
    ...
    # opposite as add except
    fridge[item] -= amount

```

## Things I see in my head
works like this
quick things you have args
(have a set list like "-r chicken breasts 2" or "-r beef min_steak 3" or "-r yogurt 50%")
("-a chicken" "-a milk 6" "-a eggs 30" )
