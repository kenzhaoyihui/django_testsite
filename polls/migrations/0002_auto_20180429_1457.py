# Generated by Django 2.0.4 on 2018-04-29 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice_texts',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question_texts',
        ),
    ]
