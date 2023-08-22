import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            dish_dict = {}
            for row in csv_reader:
                dish_name = row["dish"]
                dish_dict.setdefault(dish_name, []).append(row)

            for dish_name, dish_info in dish_dict.items():
                dish = Dish(dish_name, float(dish_info[0]["price"]))
                self.dishes.add(dish)

                for item in dish_info:
                    ingredient = Ingredient(item["ingredient"])
                    amount = int(item["recipe_amount"])
                    dish.add_ingredient_dependency(ingredient, amount)
