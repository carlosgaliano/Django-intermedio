# Generated by Django 5.0.7 on 2024-07-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.TextField(max_length=250)),
                ('year', models.TextField(max_length=4, null=True)),
            ],
        ),
    ]
