# Generated by Django 3.1.1 on 2020-09-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='choice_text',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', editable=False, max_length=30),
        ),
    ]
