# Generated by Django 5.0.6 on 2024-07-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_categoria_alter_acessorio_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Cor",
                "verbose_name_plural": "Cores",
            },
        ),
    ]
