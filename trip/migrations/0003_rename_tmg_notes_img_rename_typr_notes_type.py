# Generated by Django 5.0.3 on 2024-03-09 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_rename_reting_notes_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='tmg',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='typr',
            new_name='type',
        ),
    ]
