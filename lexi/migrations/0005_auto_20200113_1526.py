# Generated by Django 3.0 on 2020-01-13 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexi', '0004_uncommon_word'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Uncommon_Word',
            new_name='Word',
        ),
    ]
