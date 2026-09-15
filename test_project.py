import pytest
from project import add_item, search_item, format_items


def test_add_item():
    items = {}
    result = add_item(items, "Keys", "Drawer")
    assert result == "Saved 'Keys' at 'Drawer'."
    assert "keys" in items
    assert items["keys"] == ("Keys", "Drawer")

    with pytest.raises(ValueError):
        add_item(items, "", "Table")
    with pytest.raises(ValueError):
        add_item(items, "Glasses", "   ")


def test_search_item():
    items = {"wallet": ("Wallet", "Backpack")}
    
    assert search_item(items, "Wallet") == "Location of 'Wallet': Backpack"
    assert search_item(items, "wallet") == "Location of 'Wallet': Backpack"
    assert search_item(items, "Phone") == "Sorry, 'Phone' was not found."
    assert search_item(items, "") == "Please enter a valid item name to search."


def test_format_items():
    items = {}
    assert format_items(items) == "The items list is currently empty."

    items = {
        "keys": ("Keys", "Table"),
        "wallet": ("Wallet", "Bag")
    }
    output = format_items(items)
    assert "• Keys: Table" in output
    assert "• Wallet: Bag" in output
