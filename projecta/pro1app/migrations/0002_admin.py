# Generated by Django 3.2.15 on 2022-08-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
