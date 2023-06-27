from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # test 1.1 - Será validado que seu teste falha caso a
    # classe retorne hashes
    # diferentes para dois ingredientes iguais;
    ingredient = Ingredient("ovo")
    ingredient2 = Ingredient("ovo")
    assert hash(ingredient) == hash(ingredient2)

    # test 1.2 - Será validado que seu teste falha caso a classe retorne hashes
    # iguais para dois ingredientes diferentes;
    ingredient = Ingredient("ovo")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient) != hash(ingredient2)

    # test 1.3 - Será validado que seu teste falha caso a comparação de
    # igualdade de dois ingredientes iguais
    # (ou de um ingrediente com ele mesmo)
    # seja falsa;
    ingredient = Ingredient("ovo")
    ingredient2 = Ingredient("ovo")
    assert ingredient == ingredient2

    # test 1.4 - Será validado que seu teste falha caso a
    # comparação de igualdade de
    # dois ingredientes diferentes seja verdadeira;
    ingredient = Ingredient("ovo")
    ingredient2 = Ingredient("farinha")
    assert not (ingredient == ingredient2)

    # test 1.5 - Será validado que seu teste falha caso
    # a implementação do método #__repr__ retorne um valor inadequado.
    ingredient = Ingredient("ovo")
    assert repr(ingredient) == "Ingredient('ovo')"

    # test 1.6 - Será validado que seu teste falha caso
    # o atributo name de um
    # ingrediente seja diferente que o passado ao construtor.
    ingredient = Ingredient("ovo")
    assert ingredient.name == "ovo"

    # test 1.7 - Será validado que seu teste falha caso
    # o atributo restrictions de um # ingrediente não contenha
    # os valores corretos para o alimento passado.
    ingredient = Ingredient("ovo")
    expected_restrictions = {Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions

    # test 1.8 - Será validado que seu teste passa com a
    # implementação correta da
    # classe Ingredient.
    ingredient = Ingredient("farinha")
    assert ingredient.name == "farinha"
    assert ingredient.restrictions == {Restriction.GLUTEN}
