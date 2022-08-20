import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=200,
                    verbose_name='Название ингредиента'
                )),
                ('measurement_unit', models.CharField(
                    max_length=200,
                    verbose_name='Еденицы измерения'
                )),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('amount', models.PositiveSmallIntegerField(
                    validators=[django.core.validators.MinValueValidator(
                        1, message='Количество не может быть меньше 1'
                    )],
                    verbose_name='Количество ингредиента')),
            ],
            options={
                'verbose_name': 'Количество ингредиента',
                'verbose_name_plural': 'Количество ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=200,
                    verbose_name='Название рецепта')),
                ('image', models.ImageField(
                    upload_to='recipes/images/',
                    verbose_name='Изображение'
                )),
                ('text', models.TextField(verbose_name='Описание')),
                ('cooking_time', models.PositiveIntegerField(
                    validators=[django.core.validators.MinValueValidator(
                        1, message='Время приготовления должно быть больше 1 '
                                   'минуты'
                    )],
                    verbose_name='Время приготовления'
                )),
                ('pub_date', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата публикации'
                )),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=200,
                    unique=True,
                    verbose_name='Название тэга'
                )),
                ('slug', models.SlugField(
                    max_length=200,
                    unique=True,
                    verbose_name='Адрес тэга'
                )),
                ('color', models.CharField(
                    default='#49B64E',
                    max_length=7,
                    unique=True,
                    verbose_name='Цвет(HEX)'
                )),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('recipe', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='carts',
                    to='recipes.recipe',
                    verbose_name='Рецепт'
                )),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
            },
        ),
    ]
