"""
    Module name :- 0002_choice_choice_text
"""

# Generated by Django 4.2.9 on 2024-01-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    """
        Migration class.
    """
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(default="Yes", max_length=200),
            preserve_default=False,
        ),
    ]
