# Generated by Django 5.1.6 on 2025-02-15 14:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_alter_answer_next_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
