from tescos.tescos_service import TescoService


class WasteService:

    waste = {}
    tescoService = TescoService()

    def add_waste(self, name, required, units):
        actual = self.get_quanitity_from_min_units(name, units)
        self.waste[name] = {'required': required, 'actual': actual, 'waste': actual - required}
    
    def get_quanitity_from_min_units(self, name, units):
        return self.tescoService.get_quantity_from_name(name) * units

    def print_waste(self):
        for key, value in self.waste.items():
            waste = value.get('waste')
            if waste != 0:
                print(f'{key}: {waste}')