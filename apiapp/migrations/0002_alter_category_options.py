# Generated by Django 3.2.12 on 2022-03-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]