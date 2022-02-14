# Generated by Django 4.0.2 on 2022-02-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_remove_brand_gis'),
        ('gis', '0004_remove_gi_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gi',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gis', to='brands.brand'),
        ),
    ]