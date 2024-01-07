from django.db import models
from recipeingredients.models import RecipeIngredient
from ingredients.models import Ingredient

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    cooking_time = models.PositiveIntegerField(help_text="In minutes")
    description = models.TextField()
    difficulty = models.CharField(max_length=20, default="TBD")
    ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient)

    def calculate_difficulty(self):
        num_ingredients = self.ingredients.count()

        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        else:
            return "Hard"

    def __str__(self):
        return self.title