# Generated by Django 4.0.2 on 2022-02-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gis', '0001_initial'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='gis',
            field=models.ManyToManyField(blank=True, related_name='gis', to='gis.Gi'),
        ),
    ]
