import random

product_item = []

names = [
    "Web-API",
    "Laptop",
    "Wireless Mouse",
    "Mechanical Keyboard",
    "Smartphone",
    "Headphones",
    "Smart Watch",
    "USB-C Hub",
    "Bluetooth Speaker",
    "External SSD"
]

categories = [
    "API",
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Audio",
    "Wearables",
    "Accessories",
    "Audio",
    "Storage"
]

descriptions = [
    "You can Change and Upload",
    "High-performance laptop for daily use",
    "Wireless mouse with ergonomic design",
    "Mechanical keyboard with RGB lighting",
    "Latest smartphone with advanced features",
    "Wireless headphones with noise cancellation",
    "Smart watch with fitness tracking features",
    "Multi-port USB-C hub for connectivity",
    "Portable speaker with high-quality sound",
    "High-speed external storage device"
]

for i in range(1, 10001):

    index = random.randint(0, 9)

    product = {
        "id": i,
        "name": names[index],
        "category": categories[index],
        "description": descriptions[index],
        "available": random.choice([True, False])
    }

    product_item.append(product)

print("Total Products:", len(product_item))
print(product_item[:5])