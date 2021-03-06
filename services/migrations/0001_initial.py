# Generated by Django 2.0.3 on 2018-04-22 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMaster',
            fields=[
                ('customer_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('mail', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'customer_master',
            },
        ),
    ]
