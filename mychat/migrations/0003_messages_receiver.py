# Generated by Django 4.0 on 2023-11-02 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('mychat', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to='account.customusers'),
        ),
    ]
