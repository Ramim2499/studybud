# Generated by Django 5.1.2 on 2024-11-02 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_messase_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='update',
            new_name='updated',
        ),
    ]