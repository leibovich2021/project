# Generated by Django 3.2.8 on 2021-10-31 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_post_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=255),
        ),
    ]
