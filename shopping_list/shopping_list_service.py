import json
import time
from collections import defaultdict

class ShoppingListService:

    def save_dict_to_file(self, dict, file_name):
        with open(file_name, 'w') as file:
            file.write(json.dumps(dict))

    def load_dict_from_file(self, file_name):
        with open(file_name, 'r') as file:
            return json.loads(file.read())

    def get_filenames_in_recipes_folder(self):
        import os
        return os.listdir('recipes/recipeData')

    def strip_file_extension(self, filename):
        return filename.split('.')[0]

    def get_recipe_names(self):
        return [self.strip_file_extension(filename) for filename in self.get_filenames_in_recipes_folder()]

    def print_chosen_recipes(self):
        print('Here are your recipes:')
        for recipe in self.get_recipe_names():
            print(recipe)

    def print_recipes_with_index(self):
        print('\nHere are your recipes:\n')
        for index, recipe in enumerate(self.get_recipe_names()):
            print(f'{index+1}. {recipe}')

    def get_recipe_name_from_chosen_index(self, recipe_index):
        return self.get_recipe_names()[recipe_index-1]

    def get_recipe_index_from_user(self):
        recipe_index = int(input('Please enter the number of the recipe you would like to cook: '))
        return recipe_index

    def get_ingredients_from_recipe(self, recipe_name):
        recipe = self.load_dict_from_file(f'recipes/recipeData/{recipe_name}.json')
        return recipe['Ingredients']

    def create_dict_from_list(self, list):
        return {index: item for index, item in enumerate(list)}

    def concat_lists(self, list1, list2):
        return list1 + list2

    def get_spices_from_recipe(self, recipe_name):
        recipe = self.load_dict_from_file(f'recipes/recipeData/{recipe_name}.json')
        return recipe['Spices']

    def create_shopping_list(self, ingredients):
        shopping_list = defaultdict(int)
        for d in ingredients:
            shopping_list[d["Name"]] += int(d["Quantity"])
        return shopping_list

    def slow_print_dict(self, dict):
        for key, value in dict.items():
            print(f"{key}: {value}")
            time.sleep(0.05)

    def save_recipe_names_to_file(self, recipe_names):
        self.save_dict_to_file(recipe_names, 'chosen_recipes.json')

    def get_meals_and_create_shopping_list(self):
        self.print_recipes_with_index()
        print(f"\nChoose recipes to cook, enter 0 when finished")
        recipe_names = []
        while True:
            recipe_index = self.get_recipe_index_from_user()
            recipe_name = self.get_recipe_name_from_chosen_index(recipe_index)
            if recipe_index == 0:
                break
            recipe_names.append(recipe_name)
        self.save_recipe_names_to_file(recipe_names)
        ingredients = []
        for recipe in recipe_names:
            ingredients = self.concat_lists(ingredients, self.get_ingredients_from_recipe(recipe))
        shopping_list = self.create_shopping_list(ingredients)
        time.sleep(0.5)
        print("\nHere is your shopping list:")
        time.sleep(0.7)
        self.slow_print_dict(shopping_list)
        return shopping_list
