from src.models.ingredient import Ingredient
from src.models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()

        with open(self.source_path) as f:
            reader = csv.reader(f)
            next(reader)
            # dict vazio p armazenamento
            # temporário dos ingredientes de cada prato
            dish_ingredients = {}
            # iteração das linhas do csv
            for line in reader:
                dish_name = line[0]
                dish_price = float(line[1])
                ingredient_name = line[2]
                ingredient_quantity = int(line[3])

                dish = Dish(dish_name, dish_price)
                # adiciona o prato ao conjunto de pratos
                self.dishes.add(dish)
                # Verificamos se o nome do prato ainda não
                # existe em dish_ingredients.
                # Se não existir, adicionamos o nome do prato como chave
                # no dicionário e associamos uma lista vazia a ele.
                if dish_name not in dish_ingredients:
                    dish_ingredients[dish_name] = []
                # adicionamos uma tupla com nome e quantidade do ingrediente
                dish_ingredients[dish_name].append(
                    (ingredient_name, ingredient_quantity)
                )
            # depois de percorrer todas as linhas do csv,
            # iteramos sobre os pratos
            # e verificamos se o nome do prato existe em dish_ingredients.
            # Se existir, iteramos sobre os ingredientes da lista
            # e criamos uma instancia
            # de ingrediente e adicionamos a dependencia ao prato
            for dish in self.dishes:
                ingredients = dish_ingredients.get(dish.name, [])

                for ingredient_name, ingredient_quantity in ingredients:
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(
                        ingredient, ingredient_quantity
                    )
