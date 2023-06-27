from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    # test 2.1 - Será validado que seu teste falha caso o
    # atributo name de um prato seja diferente que o
    # passado ao construtor.
    dish = Dish("bolo", 10.0)
    assert dish.name == "bolo"

    # test 2.2 - Será validado que seu teste falha caso:
    #  hashes de dois pratos iguais sejam diferentes;
    dish = Dish("bolo", 10.0)
    dish2 = Dish("bolo", 10.0)
    assert hash(dish) == hash(dish2)

    # test 2.3 - Será validado que seu teste falha caso:
    # os hashes de dois pratos diferentes sejam iguais;
    dish = Dish("bolo", 10.0)
    dish2 = Dish("torta", 20.0)
    assert hash(dish) != hash(dish2)

    # test 2.4 - Será validado que seu teste falha caso:
    # a comparação de igualdade de dois pratos iguais
    # (ou de um prato com ele mesmo) seja falsa;
    dish = Dish("bolo", 10.0)
    dish2 = Dish("bolo", 10.0)
    assert dish == dish2

    # test 2.5 - Será validado que seu teste falha caso:
    # a comparação de igualdade de dois pratos
    # diferentes seja verdadeira;
    dish = Dish("bolo", 10.0)
    dish2 = Dish("torta", 20.0)
    assert not dish == dish2

    # test 2.6 - Será validado que seu teste falha caso:
    # a implementação do método __repr__
    # retorne um valor inadequado;
    dish = Dish("bolo", 10.0)
    assert repr(dish) == "Dish('bolo', R$10.00)"

    # test 2.7 - Será validado que seu teste falha caso:
    # um TypeError não seja levantado
    # ao criar um prato com um valor de tipo inválido;
    # try:
    #   Dish("sanduíche", "invalid")
    # except TypeError:
    #   pass
    # else:
    #   assert False
    with pytest.raises(TypeError):
        Dish("sanduíche", "invalid")

    # test 2.8 - Será validado que seu teste falha caso:
    # um ValueError não seja levantado ao
    # criar um prato com um valor inválido;
    # try:
    #   Dish("salada", 0)
    # except ValueError:
    #   pass
    # else:
    #   assert False
    with pytest.raises(ValueError):
        Dish("salada", 0)

    # test 2.9 - Será validado que seu teste falha caso:
    # o acesso a um valor do atributo recipe, ao ser indexado
    # com um ingrediente válido retorne uma quantidade inválida
    # dica: use o método get do dicionário,
    # por exemplo dish.recipe.get(ingredient));

    # Ajuda da Joseane para o teste 2.9 em diante
    ingredient = Ingredient("Quirera")
    dish = Dish("Quirerinha", 15.9)
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.recipe.get(ingredient) == 2

    ingredient1 = Ingredient("Quirera")
    ingredient2 = Ingredient("Costelinha")
    dish = Dish("Quirerinha", 15.9)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_restrictions() == set()

    dish = Dish("Quirerinha", 15.9)
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.get_ingredients() == {ingredient1, ingredient2}
