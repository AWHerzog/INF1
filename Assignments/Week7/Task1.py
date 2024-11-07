
class Fridge:
    def __init__(self):
        self.items = []

    def store(self, item):
        self.items.append(item)

    def take(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            raise Warning(f"Item {item[1]} with date {item[0]} not found in the fridge.")

    def find(self, name):
        matching_items = [i for i in self.items if i[1] == name]
        if not matching_items:
            return None
        return min(matching_items)
        
    def take_before(self, date):
        items_to_take = [i for i in self.items if i[0] < date]
        for item in items_to_take:
            self.items.remove(item)
        return items_to_take

    def __iter__(self):
        return iter(sorted(self.items))

    def __len__(self):
        return len(self.items)
    

f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))
print("Items in the fridge:")
for i in f:
    print(f"- {i[1]} ({i[0]})")