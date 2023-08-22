from src.models.ingredient import Restriction, Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("quejo")
    ham = Ingredient("presunto")
    butter = Ingredient("manteiga")

    assert ham.name == "presunto"
    assert cheese.__hash__() == cheese.__hash__()
    assert ham.__hash__() != butter.__hash__()
    assert cheese == cheese
    assert cheese != butter
    assert repr(butter) == "Ingredient('manteiga')"
    assert ham.restrictions == { Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT }

