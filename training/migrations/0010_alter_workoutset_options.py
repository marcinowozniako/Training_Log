# Generated by Django 4.0.4 on 2022-04-12 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_alter_workoutset_date_alter_workoutset_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workoutset',
            options={'ordering': ['date']},
        ),
    ]