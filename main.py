from recipes.recipeService import RecipeService
from shopping_list.shopping_list_service import ShoppingListService
from tescos.tescos_service import TescoService
from shopping_list.wasteService import WasteService

listService = ShoppingListService()
tescoService = TescoService()
recipeService = RecipeService()
wasteService = WasteService()

def create_shopping_list_and_update_tesco_cart():
    shopping_list = listService.get_meals_and_create_shopping_list()
    print("\nAdding To Cart...\n")
    failed_items = []
    for item in shopping_list.keys():
        try:
            min_units = tescoService.calculate_min_units_for_quantity(item, shopping_list.get(item))
            wasteService.add_waste(item, shopping_list.get(item), min_units)
            tescoService.update_amount_in_cart_by_quantity(item, min_units)
        except Exception as e:
            print(f'Error updating {item} to {shopping_list.get(item)}. Message: {e.args[0]}')
            failed_items.append(item)

    if len(failed_items) > 0:
        print(f'\nFailed to get {len(failed_items)} items: {failed_items}')
    
    print("\nWaste:")
    wasteService.print_waste()

def add_items_to_tesco_items_list():
    while True:
        print("Add items to tescos_items.json")
        name = input("Enter name: ")
        if name == 'exit':
            break
        item_id = input("Enter item id: ")
        quantity = int(input("Enter quantity: "))
        tescoService.add_tesco_item(name, item_id, quantity)
    
def add_recipe():
    recipeService.create_recipe()

def main():
    while True:
        print("\n1. Create Shopping List and Update Tesco Cart")
        print("2. Add Items To Tesco Items List")
        print("3. Add Recipe")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            create_shopping_list_and_update_tesco_cart()
        elif choice == '2':
            add_items_to_tesco_items_list()
        elif choice == '3':
            add_recipe()
        elif choice == '4':
            exit()
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()