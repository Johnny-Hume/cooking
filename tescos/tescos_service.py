import json
import math
from urllib import response
from tescos.tescos_proxy import TescoProxy

class TescoService:

    tescoProxy = TescoProxy()

    def load_tesco_items_json(self):
        with open('tescos/tesco_items.json') as json_file:
            return json.load(json_file)

    def pretty_print_json(self, json_data):
        print(json.dumps(json_data, indent=4))

    def get_id_from_name(self, name):
        try:
            return self.load_tesco_items_json().get('Items').get(name).get('id')
        except Exception as e:
            raise Exception(f'{name} not found in tescos_items.json')
        
    def get_quantity_from_name(self, name):
        try:
            return self.load_tesco_items_json().get('Items').get(name).get('quantity')
        except Exception as e:
            raise Exception(f'{name} not found in tescos_items.json')

    def update_amount_in_cart_by_name(self, name, amount):
        id = self.get_id_from_name(name)
        return self.tescoProxy.update_amount_in_cart(id, amount)

    def round_up_decimal(self, decimal):
        return math.ceil(decimal)

    def calculate_min_units_for_quantity(self, name, required_quantity):
        quantity_per_item = self.get_quantity_from_name(name)
        exact_units_needed = required_quantity / quantity_per_item
        return self.round_up_decimal(exact_units_needed)

    def update_amount_in_cart_by_quantity(self, name, amount):
        response_code = self.update_amount_in_cart_by_name(name, amount)
        if response_code == 200:
            print(f'Updated {name} to {amount}')
        else:
            raise Exception(f'Error Status: {response_code} updating {name} to {amount}')

    def add_tesco_item(self, name, item_id, quantity):
        tescos_items = self.load_tesco_items_json()
        tescos_items.get('Items').update({name: {'id': item_id, 'quantity': quantity}})
        with open('tescos/tesco_items.json', 'w') as outfile:
            json.dump(tescos_items, outfile)
        print("Item added")

