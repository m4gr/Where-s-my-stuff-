import csv
import sys

FILE_NAME = "items.csv"


def main():
    items = load_items(FILE_NAME)

    while True:
        print("\n=== Where's My Stuff? ===")
        print("1. Add item and location")
        print("2. Search for an item")
        print("3. View all items")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            location = input("Item location: ").strip()
            try:
                msg = add_item(items, name, location)
                save_items(FILE_NAME, items)
                print(f"\n✅ {msg}")
            except ValueError as e:
                print(f"\n❌ Error: {e}")

        elif choice == "2":
            name = input("What are you looking for?: ").strip()
            result = search_item(items, name)
            print(f"\n🔍 {result}")

        elif choice == "3":
            print("\n" + format_items(items))

        elif choice == "4":
            print("\nGoodbye! Hope you always find what you're looking for.")
            sys.exit(0)

        else:
            print("\n❌ Invalid choice. Please select an option from 1 to 4.")


def add_item(items, name, location):
    """Adds a new item and its location to the dictionary with validation."""
    clean_name = name.strip() if name else ""
    clean_location = location.strip() if location else ""

    if not clean_name or not clean_location:
        raise ValueError("Item name and location cannot be empty.")

    items[clean_name.lower()] = (clean_name, clean_location)
    return f"Saved '{clean_name}' at '{clean_location}'."


def search_item(items, name):
    """Searches for an item's location (case-insensitive)."""
    if not name or not name.strip():
        return "Please enter a valid item name to search."

    key = name.strip().lower()
    if key in items:
        original_name, location = items[key]
        return f"Location of '{original_name}': {location}"
    
    return f"Sorry, '{name}' was not found."


def format_items(items):
    """Formats all stored items into a readable string list."""
    if not items:
        return "The items list is currently empty."

    lines = ["📋 Stored Items and Locations:"]
    lines.append("-" * 35)
    for original_name, location in sorted(items.values()):
        lines.append(f"• {original_name}: {location}")
    lines.append("-" * 35)
    return "\n".join(lines)


def load_items(filename):
    """Loads stored items from a CSV file."""
    items = {}
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    original_name, location = row
                    items[original_name.lower()] = (original_name, location)
    except FileNotFoundError:
        pass
    return items


def save_items(filename, items):
    """Saves items dictionary into a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for original_name, location in items.values():
            writer.writerow([original_name, location])


if __name__ == "__main__":
    main()
