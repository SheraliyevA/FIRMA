# Generated by Django 5.0.2 on 2024-02-16 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0011_alter_mahsulot_mahsulot_id_alter_missed_xodim_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missed',
            name='xodim_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firma.xodim'),
        ),
    ]
