# Generated by Django 5.0.1 on 2024-01-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_accountnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='accountNumber',
            field=models.CharField(max_length=20),
        ),
    ]