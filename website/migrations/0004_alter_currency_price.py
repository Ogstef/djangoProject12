# Generated by Django 4.0.3 on 2022-04-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_currency_date_achieved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=7),
        ),
    ]
