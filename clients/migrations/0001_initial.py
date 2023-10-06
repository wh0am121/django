import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('surname', models.CharField(max_length=200, verbose_name='Surname')),
                ('street_address', models.CharField(max_length=200, verbose_name='Address')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('postal_code', models.CharField(max_length=6, verbose_name='Postcode')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(choices=[('Property', 'Property insurance'),
                                                             ("Emergency", "Contingency insurance"),
                                                             ("Life", "Life insurance"),
                                                             ("Accident", "Accident insurance"),
                                                             ("Responsibility", "Civil liability insurance")],
                                                    max_length=30, verbose_name='Insurance type')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject of insurance')),
                ('amount', models.PositiveIntegerField(verbose_name='Sum insured')),
                ('date_from', models.DateField(default=datetime.date.today, verbose_name='Date from')),
                ('date_to', models.DateField(default=datetime.date.today, verbose_name='Date to')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
