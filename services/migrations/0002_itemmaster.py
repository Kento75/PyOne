# Generated by Django 2.0.3 on 2018-05-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
