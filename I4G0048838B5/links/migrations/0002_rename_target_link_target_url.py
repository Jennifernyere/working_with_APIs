# Generated by Django 4.0.5 on 2022-07-02 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='target',
            new_name='target_url',
        ),
    ]