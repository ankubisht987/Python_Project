import json
from Data_Create_From import product_item

with open("products.json", "w") as file:
    json.dump(product_item, file, indent=4)

print("10,000 products created successfully!")