# Generated by Django 4.2.6 on 2023-10-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentRating',
            field=models.SmallIntegerField(default=0),
        ),
    ]