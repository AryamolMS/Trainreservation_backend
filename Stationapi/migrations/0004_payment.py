# Generated by Django 4.2.4 on 2024-02-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stationapi', '0003_rename_username_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('failed', 'failed')], default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stationapi.customer')),
            ],
        ),
    ]
