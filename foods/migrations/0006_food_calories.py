# Generated by Django 5.1.3 on 2024-11-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_remove_food_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
