# Generated by Django 3.2.8 on 2021-10-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=1, verbose_name=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
