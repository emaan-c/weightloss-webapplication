# Generated by Django 3.2.2 on 2021-05-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(max_length=20)),
                ('calories', models.CharField(max_length=20)),
                ('food_type1', models.CharField(max_length=20)),
                ('calories1', models.CharField(max_length=20)),
                ('food_type2', models.CharField(max_length=20)),
                ('calories2', models.CharField(max_length=20)),
                ('food_type3', models.CharField(max_length=20)),
                ('calories3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=16)),
                ('weight', models.CharField(max_length=64)),
            ],
        ),
    ]