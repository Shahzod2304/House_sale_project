# Generated by Django 4.2.4 on 2023-10-09 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0005_remove_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='description',
        ),
    ]
