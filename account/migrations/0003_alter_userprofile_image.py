# Generated by Django 4.0 on 2023-11-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profiles/user.png', upload_to='profiles'),
        ),
    ]
