# Generated by Django 5.1.6 on 2025-02-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_limit', models.DateField(blank=True, null=True)),
                ('totalScore', models.IntegerField(default=0)),
            ],
        ),
    ]
