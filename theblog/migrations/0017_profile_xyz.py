# Generated by Django 4.2.1 on 2023-07-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='xyz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
