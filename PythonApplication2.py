class Item:
    def __init__(self, name, price, description, category, rating):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.rating = rating

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.purchase_history = []

    def make_purchase(self, order):
        self.purchase_history.append(order)

class Order:
    def __init__(self, items, quantities):
        self.items = items
        self.quantities = quantities
        self.status = "Pending"
        self.total_price = sum(item.price * quantity for item, quantity in zip(items, quantities))

class Shop:
    def __init__(self):
        self.items = []  # Список товарів
        self.users = []  # Список користувачів

    def add_item(self, item):
        self.items.append(item)

    def add_user(self, user):
        self.users.append(user)

    def search_items(self, criteria):
        # Реалізуйте пошук товарів за заданими критеріями (ціна, категорія, рейтинг)
        result = []
        for item in self.items:
            if criteria(item):
                result.append(item)
        return result

# Приклад використання:

# Створення товарів
item1 = Item("Laptop", 1000, "Powerful laptop", "Electronics", 4.5)
item2 = Item("Book", 20, "Bestseller book", "Books", 4.8)
item3 = Item("Phone", 500, "Smartphone", "Electronics", 4.0)

# Створення користувачів
user1 = User("user1", "password1")
user2 = User("user2", "password2")

# Створення замовлення
order1 = Order([item1, item2], [1, 2])
order2 = Order([item3], [1])

# Зробити покупку користувачем
user1.make_purchase(order1)
user2.make_purchase(order2)

# Створення магазину і додавання товарів та користувачів
shop = Shop()
shop.add_item(item1)
shop.add_item(item2)
shop.add_item(item3)
shop.add_user(user1)
shop.add_user(user2)

# Пошук товарів за критеріями (приклад - товари з категорією "Electronics"):
result = shop.search_items(lambda item: item.category == "Electronics")
for item in result:
    print(f"Found item: {item.name}")

