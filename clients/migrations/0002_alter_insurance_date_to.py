import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='date_to',
            field=models.DateField(default=datetime.date.today, verbose_name='Date to'),
        ),
    ]
