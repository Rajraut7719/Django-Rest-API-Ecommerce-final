# Generated by Django 3.2.12 on 2022-03-30 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tag', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imgeUrl', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='apiapp.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
                ('imgeUrl', models.URLField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='apiapp.category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
