# Generated by Django 5.0.2 on 2024-02-16 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0010_alter_xodim_ism'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='mahsulot_id',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='missed',
            name='xodim_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firma.xodim', unique=True),
        ),
    ]