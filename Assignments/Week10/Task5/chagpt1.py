def summarize_products(products):
    return {
        category: sum(quantity for _, cat, quantity in products if cat == category)
         for category in {cat for _, cat, _ in products}
    }

# Example usage:
products = [
    ('Laptop', 'Electronics', 5),
    ('Headphones', 'Electronics', 8),
    ('Banana', 'Groceries', 12),
    ('Apple', 'Groceries', 15),
    ('Shirt', 'Clothing', 7),
    ('Pants', 'Clothing', 6),
    ('TV', 'Electronics', 3),
    ('Orange', 'Groceries', 10)
]
print(summarize_products(products))


'''
{
    'Electronics': 16,
    'Groceries': 37,
    'Clothing': 13
}
'''