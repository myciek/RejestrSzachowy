# Generated by Django 3.2.4 on 2021-06-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_alter_match_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.IntegerField(choices=[(1, 'Biale'), (2, 'Remis'), (3, 'Czarne')]),
        ),
    ]
