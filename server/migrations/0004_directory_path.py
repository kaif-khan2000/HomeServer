# Generated by Django 3.1 on 2020-09-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20200928_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='path',
            field=models.CharField(default='/', max_length=500),
        ),
    ]
