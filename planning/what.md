# What I want to make

## main stuff
1. A file with your current inventory and levels.
2. A way to view inventory.
3. A way to update the inventory (If you use things or bought new stuff)
4. A grocery list part
   1. Remind you whats low
   2. make a grocery list automatically based on whats low

### function
init fridge
load
view
add
remove

list parts
check levels
reminder
make a list as a txt file

(check the todo list and scaffold for tips)

## Other

- Planning out JSON File


have it so main.py has fancy looking stuff but the other py files just have clean data to work with

so grocery has all the code and main is just calling it

so as we been over the following

Inventory goes into a dictionary and every item is a dictionary paired with the item

can also have argparse for quick updates
like gimme list
I got milk

## From obsidian

loading the json into something that makes sense
**NEED TO RESEARCH THIS**

now something that can add, remove and edit the json variable

Then something for grocery list

```python
import json

with open("fridge.json", "r") as f:
	data = json.load(f)
	
'''
then you can work with data and just export it to the file in the end
eg:
'''
def add_item(data,item):
	if item in data["fridge"]:
		# somehow get the index (which is the same as the item)
		data[fridge][index][amount] += 1
		with open("fridge.json", "w") as f:
			json.dump(data, f) 
```