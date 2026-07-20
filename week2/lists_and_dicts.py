# lists_and_dicts.py

# Lists
items = ["Web Design", "Hosting", "Domain"]
prices = [2500, 1200, 150]

print("First item:", items[0])
print("Number of items:", len(items))

# Add new item
items.append("SEO Package")
print("Updated list:", items)

# Dictionaries
invoice = {
    "customer": "John Doe",
    "date": "2026-07-13",
    "total": 3850.00
}

print("Customer:", invoice["customer"])
print("Total:", invoice["total"])
