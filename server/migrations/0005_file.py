# Generated by Django 3.1 on 2020-09-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_directory_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('typeOfFile', models.CharField(max_length=5)),
                ('size', models.CharField(max_length=20)),
                ('actual_file', models.FileField(upload_to='static/content')),
                ('uploaded_on', models.DateField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.directory')),
            ],
        ),
    ]
