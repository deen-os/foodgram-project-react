from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.CharField(
                max_length=20, verbose_name='Еденицы измерения'
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(
                max_length=20, unique=True, verbose_name='Название тэга'
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(
                max_length=20, unique=True, verbose_name='Адрес тэга'
            ),
        ),
    ]
