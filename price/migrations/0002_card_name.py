# Generated by Django 4.1.2 on 2022-10-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(default='BRONZE', max_length=20),
        ),
    ]
