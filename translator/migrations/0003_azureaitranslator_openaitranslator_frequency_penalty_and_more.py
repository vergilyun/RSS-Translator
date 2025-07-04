# Generated by Django 5.0.1 on 2024-01-25 12:00

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translator", "0002_openaitranslator_base_url_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AzureAITranslator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                ("valid", models.BooleanField(null=True, verbose_name="Valid")),
                (
                    "api_key",
                    encrypted_model_fields.fields.EncryptedCharField(
                        verbose_name="API Key"
                    ),
                ),
                (
                    "endpoint",
                    models.URLField(
                        default="https://example.openai.azure.com/",
                        verbose_name="Endpoint",
                    ),
                ),
                (
                    "version",
                    models.CharField(default="2023-12-01-preview", max_length=50),
                ),
                ("deloyment_name", models.CharField(max_length=100)),
                (
                    "prompt",
                    models.TextField(
                        default="Translate the following to {target_language},only returns translations.\n{text}"
                    ),
                ),
                ("temperature", models.FloatField(default=0.5)),
                ("top_p", models.FloatField(default=0.95)),
                ("frequency_penalty", models.FloatField(default=0)),
                ("presence_penalty", models.FloatField(default=0)),
                ("max_tokens", models.IntegerField(default=1000)),
            ],
            options={
                "verbose_name": "Azure OpenAI",
                "verbose_name_plural": "Azure OpenAI",
            },
        ),
        migrations.AddField(
            model_name="openaitranslator",
            name="frequency_penalty",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="openaitranslator",
            name="presence_penalty",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="openaitranslator",
            name="top_p",
            field=models.FloatField(default=0.95),
        ),
    ]
