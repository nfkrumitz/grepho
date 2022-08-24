# Generated by Django 3.0 on 2022-08-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0007_auto_20220824_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='propbalcon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='house',
            name='propchambr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='propcuisine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='house',
            name='propdouche',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='propsalemanger',
            field=models.BooleanField(default=False),
        ),
    ]
