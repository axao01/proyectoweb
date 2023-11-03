# Generated by Django 4.2.6 on 2023-10-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField(max_length=4)),
                ('humedad', models.FloatField(max_length=4)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
