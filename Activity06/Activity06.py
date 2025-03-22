class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Price: {self.price}"

class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("Warning: Item ID already exists. Updating item instead.")
            self.update_item(item.item_id, item.name, item.description, item.price)
            return
        self.items[item.item_id] = item
        print(f"Added: {item}")

    def get_item(self, item_id):
        return self.items.get(item_id, "Item not found")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        
        item = self.items[item_id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            item.price = price
        print(f"Updated: {item}")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Deleted item with ID: {item_id}")
        else:
            print("Error: Item not found.")

    def list_items(self):
        if not self.items:
            print("No items in inventory.")
            return
        for item in self.items.values():
            print(item)

if __name__ == "__main__":
    manager = ItemManager()
    item1 = Item(1, "Midnight Cake", "A delicious cream cheese-based cake with blueberry sauce on top", 275)
    manager.add_item(item1)

    item2 = Item(2, "Crimson Embrace", "A luscious red velvety cake covered and filled with cream cheese", 285)
    manager.add_item(item2)

    print("\nItems in inventory:")
    manager.list_items()

    manager.update_item(1, price=285)
    print("\nAfter updating item 1:")
    print(manager.get_item(1))

    manager.delete_item(2)
    print("\nAfter deleting item 2:")
    manager.list_items()

    item_duplicate = Item(1, "Autumn Harvest", "Fresh chiffon cake mixed with carrot bits and covered with buttercup frosting", 270)
    manager.add_item(item_duplicate)
