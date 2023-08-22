from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction, Ingredient
import pytest


# Req 2
def test_dish():
    cheese = Dish("queijo", 10)
    ham = Dish("presunto", 7)

    ingredient_ham = Ingredient('presunto')

    assert cheese.name == "queijo"
    assert cheese.__hash__() == cheese.__hash__()
    assert cheese.__hash__() != ham.__hash__()
    assert cheese == cheese
    assert cheese != ham
    assert repr(cheese) == "Dish('queijo', R$10.00)"

    cheese.add_ingredient_dependency(ingredient_ham, 5)
    assert cheese.get_restrictions() == {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert cheese.get_ingredients() == {Ingredient('presunto')}

    with pytest.raises(TypeError):
        Dish('Potato', '-10')

    with pytest.raises(ValueError):
        Dish("butter", -10)
