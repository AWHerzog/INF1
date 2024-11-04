
class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = {}

    def ingredients_for_servings(self, amount):
        
        for i in self.ingredients:
            i * amount

            return i    
    def __str__(self):
        return f"A recipe for {self.name}"
    
    def __repr__(self):
        pass
    

class DietRecipe(Recipe):
    def __init__(self, name, ingredients, calories):
        super().__init__(name, ingredients)
        self.calories = calories

    def servings_for_calories(self, permissable):
        return permissable / self.calories




