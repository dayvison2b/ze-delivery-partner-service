# Generated by Django 5.0.3 on 2024-03-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]