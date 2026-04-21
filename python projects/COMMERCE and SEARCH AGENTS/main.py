from rich.prompt import Prompt
import json
INVENTORY__FILE = "inventory.txt"
PRODUCT_FILE = "product_specification.json"

# product_prompt = Prompt.ask('What do you seek? ').upper().strip().rsplit(sep= " ")
# product_name = product_prompt[1]

def productCheck(item, inventory_dict):
    is_present: bool = False
    if item in inventory_dict:
        is_present = True
        return is_present
    else:
        return f"Error 404: could not be found"

def furtherProductSpecification():
    pass
    # test1
    # test2
    # test3
    # test4

def fetchInventory():
    with open(INVENTORY__FILE, "r") as file:
        available_items = {}
        for line in file:
            indexed_item, available_units = line.strip().split(",")
            available_items[indexed_item] = available_units
    return available_items


with open(PRODUCT_FILE, "r") as file:
    content = json.load(file)
    for line in content:
        print(line)