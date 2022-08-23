import csv
import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Command(BaseCommand):
    def handle(self, *args, **options):
        Ingredient.objects.all().delete()
        logging.info(' Модель Ingredient базы данных очищена.')
        base_parent_dir = os.path.abspath(
            os.path.join(settings.BASE_DIR, os.pardir)
        )
        ingredients = os.path.join(base_parent_dir, 'data', 'ingredients.csv')
        with open(ingredients, encoding='utf-8') as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                if counter % 100 == 0:
                    logging.info(f' Добавлен ингридиент {row[0]}')
                Ingredient.objects.create(name=row[0], measurement_unit=row[1])
                counter += 1
        logging.info(
            f' В базу данных успешно добавлены ингредиенты - {counter} шт.'
        )
