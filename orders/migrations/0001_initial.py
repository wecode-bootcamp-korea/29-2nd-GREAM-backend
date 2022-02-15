# Generated by Django 4.0.2 on 2022-02-16 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_id', to='users.user')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller_id', to='users.user')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='orders.status')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
