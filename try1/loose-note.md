# Just loose thoughts

## testing
for testing the file have something life this
```python
current_state = "the nice looking json"
grocery = json.dumps(current_state)

update_json(grocery)
# here you would do something that compares the current_state and actual json file


load_grocery()
# here you have something to make sure it gets whats in file, if the file is invalid stuff
```