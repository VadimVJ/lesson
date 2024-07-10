class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте магазина '{self.name}'.")

# Пример использования
store1 = Store("Магазин продуктов", "ул. Центральная 1")
store1.add_item("Яблоки", 1.0)
store1.add_item("Молоко", 0.75)

print(store1.get_item_price("Яблоки"))
store1.update_item_price("Яблоки", 1.5)
store1.remove_item("Молоко")
store1.remove_item("Хлеб")