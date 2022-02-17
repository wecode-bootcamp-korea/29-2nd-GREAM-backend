# Generated by Django 4.0.2 on 2022-02-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kakao', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
