inventory = {
    'apple': {'quantity': 10, 'price': 0.5},
    'banana': {'quantity': 0, 'price': 0.3},
    'orange': {'quantity': 5, 'price': 0.8}
}

def calculate_quantity(inventory):
    return {
        produce: {
            'quantity': details['quantity'],
            'price': details['price'],
            'total_value': details['quantity'] * details['price']
        }
        for produce, details in inventory.items() if details['quantity'] > 0
    }


inventory = {
    'apple': {'quantity': 10, 'price': 0.5},
    'banana': {'quantity': 0, 'price': 0.3},
    'orange': {'quantity': 5, 'price': 0.8}
}

print(calculate_quantity(inventory))



print(calculate_quantity(inventory))
#luiz
