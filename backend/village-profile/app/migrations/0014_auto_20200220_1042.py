# Generated by Django 2.1.3 on 2020-02-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200220_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='foreign_stay',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
