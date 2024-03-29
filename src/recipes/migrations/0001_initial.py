# Generated by Django 5.0.1 on 2024-01-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
        ('recipeingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cooking_time', models.PositiveIntegerField(help_text='In minutes')),
                ('description', models.TextField()),
                ('difficulty', models.CharField(default='TBD', max_length=20)),
                ('ingredients', models.ManyToManyField(through='recipeingredients.RecipeIngredient', to='ingredients.ingredient')),
            ],
        ),
    ]
