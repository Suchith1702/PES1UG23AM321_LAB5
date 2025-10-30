"""
inventory_system.py
-------------------
A simple inventory management system that allows adding, removing, loading,
saving, and checking items with quantities. Data is stored in JSON format.
"""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The name of the item.
        qty (int | float): Quantity to add.
        logs (list, optional): A list to store action logs.

    Returns:
        None
    """
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        return
    if qty < 0:
        print(f"Warning: Negative quantity for {item} ignored.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove a specific quantity of an item from the inventory.

    Args:
        item (str): The name of the item.
        qty (int | float): Quantity to remove.

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Tried to remove missing item '{item}'")


def get_qty(item):
    """
    Get the quantity of a specific item.

    Args:
        item (str): The name of the item.

    Returns:
        int | float: The quantity available in stock.
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): Path to the inventory JSON file.

    Returns:
        None
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        stock_data.clear()


def save_data(file="inventory.json"):
    """
    Save the current inventory data to a JSON file.

    Args:
        file (str): Path to the inventory JSON file.

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """
    Print all inventory items and their quantities.

    Returns:
        None
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Get a list of items whose stock is below the given threshold.

    Args:
        threshold (int | float): The minimum quantity threshold.

    Returns:
        list: Items with stock below the threshold.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """
    Demonstrate inventory operations such as adding, removing,
    saving, loading, and printing data.

    Returns:
        None
    """
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("grapes", 5)
    # remove_item("apple", 3)  # Removed to keep apple = 10
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":  # ✅ Corrected
    main()
