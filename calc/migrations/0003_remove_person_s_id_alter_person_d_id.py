# Generated by Django 4.0.4 on 2022-06-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_alter_person_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='s_id',
        ),
        migrations.AlterField(
            model_name='person',
            name='d_id',
            field=models.BooleanField(default=True),
        ),
    ]