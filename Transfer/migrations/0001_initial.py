# Generated by Django 4.0.4 on 2022-05-15 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('CREDIT', 'Credit'), ('DEBIT', 'Debit')], default='DEBIT', max_length=6)),
                ('transaction_balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('From_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_accno', to='Account.userbankaccount')),
                ('To_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_accno', to='Account.userbankaccount')),
            ],
        ),
    ]
