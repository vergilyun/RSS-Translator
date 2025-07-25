# Generated by Django 5.0.6 on 2024-05-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translator", "0027_alter_azureaitranslator_api_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="azureaitranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="azureaitranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="azureaitranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="groqtranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="groqtranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="groqtranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="moonshotaitranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="moonshotaitranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="moonshotaitranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="openaitranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="openaitranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="openaitranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="openrouteraitranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="openrouteraitranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="openrouteraitranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="togetheraitranslator",
            name="max_tokens",
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name="togetheraitranslator",
            name="temperature",
            field=models.FloatField(default=0.2),
        ),
        migrations.AlterField(
            model_name="togetheraitranslator",
            name="top_p",
            field=models.FloatField(default=0.2),
        ),
    ]
