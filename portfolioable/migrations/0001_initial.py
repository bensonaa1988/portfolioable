# Generated by Django 4.0.6 on 2022-07-29 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2000)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioable.portfolio')),
            ],
        ),
    ]