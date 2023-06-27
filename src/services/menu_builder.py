from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        # testando o uso de list comprehension
        # 1 é criado uma lista contendo os dicionários de cada prato
        # 2 em seguida é aplicado uma segunda filtragem para remover
        # os pratos cujo ingredientes não estão disponíveis no estoque
        main_menu = [
            # cria um dicionário para cada prato elegível
            {
                "dish_name": dish.name,
                "ingredients": list(dish.get_ingredients()),
                "price": dish.price,
                "restrictions": list(dish.get_restrictions()),
            }
            for dish in self.menu_data.dishes
            # Apenas os pratos que atendem a essa condição
            # são considerados elegíveis para o menu.
            if restriction is None
            or restriction not in dish.get_restrictions()
        ]
        # Utiliza uma nova compreensão de lista para filtrar
        # os pratos elegíveis do menu com base na
        # disponibilidade de ingredientes
        main_menu = [
            menu_item
            for menu_item in main_menu
            # retorna true se todas as condições forem verdadeiras
            if all(
                # Verifica se a quantidade de cada ingrediente
                # (ingredient) necessária para o prato
                # é maior que zero no inventário
                self.inventory.inventory.get(ingredient, 0) > 0
                # Percorre todos os ingredientes do prato
                # (menu_item["ingredients"]).
                for ingredient in menu_item["ingredients"]
            )
        ]
        # retorna  contendo os dicionários dos pratos
        # elegíveis que possuem ingredientes disponíveis no inventário.
        return main_menu
