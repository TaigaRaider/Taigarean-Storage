from rich.prompt import Prompt

INVENTORY__FILE = "inventory.txt"

Product = Prompt.ask('What do you seek? ')


def productCheck(item, inventory_dict):
    is_present: bool = False

    if item in inventory_dict:
        is_present = True

        return is_present
    else:
        return f"Error 404: Item could not be found"


def fetchInventory():
    with open(INVENTORY__FILE, "r") as file:
        available_items = {}
        for line in file:
            indexed_item, available_units = line.strip().split(",")
            available_items[indexed_item] = available_units
    return available_items


print(inventoryCheck(Product, displayInventory()))
