# Generated by Django 5.0.6 on 2024-05-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('disc', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
