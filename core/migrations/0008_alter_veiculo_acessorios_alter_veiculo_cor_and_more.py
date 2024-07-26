# Generated by Django 5.0.6 on 2024-07-23 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_veiculo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="acessorios",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.acessorio"),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="cor",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.cor"),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="modelo",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.modelo"),
        ),
    ]
