# Generated by Django 5.0.3 on 2024-03-16 19:44

import django.contrib.gis.db.models.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tradingName', models.CharField(max_length=255)),
                ('ownerName', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=18, unique=True)),
                ('coverageArea', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('address', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
