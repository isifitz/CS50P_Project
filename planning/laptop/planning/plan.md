# 🧺 CS50P Final Project Plan — Grocery List Manager

## Overview
The **Grocery List Manager** is a command-line Python program that helps users manage their household inventory and automatically generates a grocery list for low-stock items.

It will:
- Store all inventory data in a local JSON file.
- Allow users to view and update inventory.
- Automatically generate a grocery list based on thresholds.
- Emphasize clean, testable code and modular design.

____
## 🎯 Features

1. **Persistent inventory file** (`inventory.json`)  
   Stores items, quantities, and thresholds.
2. **View inventory**  
   Displays all current items and stock levels.
3. **Update inventory**  
   Add, remove, or adjust quantities for items.
4. **Grocery list generator**  
   Automatically detects low-stock items and suggests what to buy.
5. **Optional extras**  
   - Export grocery list to text file  
   - Adjust thresholds interactively  
   - Sort or filter inventory display

____
## 🧱 Data Structure

Example `inventory.json`:

```json
{
  "milk": {"quantity": 1, "threshold": 2},
  "bread": {"quantity": 3, "threshold": 1},
  "eggs": {"quantity": 0, "threshold": 6}
}
```
____
## 🗂 File Structure

```
grocery_manager/
├── main.py           # CLI menu and main logic
├── grocery.py        # Core functions
├── inventory.json    # Inventory data
├── tests.py          # Automated tests
└── README.md         # Documentation for submission
```

⸻
## 🗓️ 5-Day Plan

### Day 1 – Design & Setup

Goals:
•	Plan program logic and data structure.
•	Set up project files and write basic file I/O.

Tasks:
•	Create all starter files and folders.
•	Define functions in grocery.py:
```py
def load_inventory(filename="inventory.json") -> dict: ...
def save_inventory(data, filename="inventory.json"): ...
```

•	Add sample data to inventory.json.
•	Test loading/saving manually:
```py
inv = load_inventory()
print(inv)
save_inventory(inv)
```

Outcome:
✅ Inventory file structure ready
✅ Load/save functions working

⸻
### Day 2 – Core Features

Goals:
Implement all main functions for managing inventory.

Tasks:
•	Add these functions to grocery.py:
```py
def view_inventory(inventory): ...
def add_item(inventory, name, quantity, threshold): ...
def remove_item(inventory, name): ...
def update_item(inventory, name, change): ...
def generate_grocery_list(inventory): ...

```
•	Test them with small sample inventories in tests.py.
Example tests:
```py
inv = {
    "milk": {"quantity": 1, "threshold": 2},
    "bread": {"quantity": 2, "threshold": 1}
}
assert generate_grocery_list(inv) == ["milk"]
```

Outcome:
✅ Inventory manipulation fully functional
✅ Grocery list generation works

⸻
### Day 3 – CLI Interface

Goals:
Build a text-based user interface in main.py.

Tasks:
•	Add a menu loop:
```py
def main():
    inv = load_inventory()
    while True:
        print("\n1. View inventory\n2. Add item\n3. Update item\n4. Grocery list\n5. Quit")
        choice = input("Choose: ")
        # Call appropriate functions
```
•	Ensure program saves automatically before exiting.
•	Keep logic modular — functions do the heavy lifting, CLI only handles input/output.

Outcome:
✅ CLI allows basic interaction
✅ All functions callable through menu

⸻
### Day 4 – Testing & Error Handling

Goals:
Write automated tests, handle user and file errors gracefully.

Tasks:
•	Add proper exception handling:
•	Invalid item names
•	Non-numeric quantities
•	Missing or corrupted JSON file
•	Expand tests.py:
•	Test for correct function outputs.
•	Test that errors are handled cleanly.
```py
import pytest
def test_update_missing_item():
    inv = {}
    with pytest.raises(KeyError):
        update_item(inv, "milk", 1)
```
•	Run tests until all pass.
•	Add type hints and docstrings to all functions.

Outcome:
✅ Program handles bad input safely
✅ All tests pass cleanly

⸻
### Day 5 – Polishing & Documentation

Goals:
Refine code, improve readability, and prepare for submission.

Tasks:
•	Add comments and clear variable names.
•	Review user prompts and messages for clarity.
•	Write README.md:
•	What the project does
•	How to run it
•	Example usage
•	Optional enhancements:
•	Export grocery list to text file.
•	Add colorized output using rich.
•	Sort inventory by name or quantity.

Outcome:
✅ Code clean and readable
✅ Fully functional and documented project ready for submission

⸻
## 🧪 Testing Strategy

Keep functions deterministic and side-effect-free where possible.
Each can be tested in isolation, for example:
```py
def test_generate_grocery_list():
    inv = {
        "milk": {"quantity": 1, "threshold": 2},
        "bread": {"quantity": 3, "threshold": 1}
    }
    assert generate_grocery_list(inv) == ["milk"]
```
Tests should cover:
•	Loading/saving JSON
•	Adding/updating/removing items
•	Low-stock detection
•	Invalid input handling

⸻

## ✅ Submission Checklist
•	Program runs via python main.py
•	Uses JSON for data storage
•	Implements all core features
•	Handles user and file errors
•	Includes automated tests
•	Includes clear README with examples
•	Code style clean and modular

⸻
## 🧩 Stretch Ideas (Optional)
•	Category field for each item (e.g., “Dairy”, “Produce”)
•	Date added or last updated tracking
•	Config file for setting default thresholds
•	Weekly summary of items used/bought

⸻