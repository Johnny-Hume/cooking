import json
class RecipeService:

    def create_recipe(self):
        name = input("Enter recipe name: ")
        ingredients = []
        while True:
            ingredient = input("Enter ingredient: ")
            if ingredient == 'exit':
                break
            quantity = input("Enter quantity: ")
            ingredients.append({
                'Name': ingredient,
                'Quantity': quantity
            })
        self.save_recipe_to_json(name, ingredients)

    def save_recipe_to_json(self, name, ingredients):
        recipe = {
            'Ingredients': ingredients
        }
        self.save_dict_to_file(recipe, f'recipes/recipeData/{name}.json')
    
    def save_dict_to_file(self, dict, file_name):
        with open(file_name, 'w+') as f:
            json.dump(dict, f)
        print(f"Saved {file_name}")