# Generated by Django 2.0.3 on 2018-05-18 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_itemmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_datetime', models.DateTimeField(verbose_name='販売日時')),
                ('customer_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.CustomerMaster')),
            ],
            options={
                'db_table': 'sales_history',
            },
        ),
        migrations.AlterModelTable(
            name='itemmaster',
            table='item_master',
        ),
        migrations.AddField(
            model_name='saleshistory',
            name='item_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.ItemMaster'),
        ),
    ]
