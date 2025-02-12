from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="(e.g. SETTING_NAME)",
                        max_length=50,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "value_type",
                    models.CharField(
                        choices=[
                            ("bool", "bool"),
                            ("date", "date"),
                            ("datetime", "datetime"),
                            ("decimal", "decimal"),
                            ("email", "email"),
                            ("file", "file"),
                            ("float", "float"),
                            ("image", "image"),
                            ("int", "int"),
                            ("string", "string"),
                            ("text", "text"),
                            ("time", "time"),
                            ("url", "url"),
                        ],
                        max_length=20,
                        verbose_name="Type",
                    ),
                ),
                (
                    "value_bool",
                    models.BooleanField(default=False, verbose_name="Value"),
                ),
                (
                    "value_date",
                    models.DateField(blank=True, null=True, verbose_name="Value"),
                ),
                (
                    "value_datetime",
                    models.DateTimeField(blank=True, null=True, verbose_name="Value"),
                ),
                (
                    "value_decimal",
                    models.DecimalField(
                        blank=True,
                        decimal_places=10,
                        default=Decimal("0.0"),
                        max_digits=19,
                        verbose_name="Value",
                    ),
                ),
                (
                    "value_email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Value"),
                ),
                (
                    "value_file",
                    models.FileField(
                        blank=True, upload_to="files", verbose_name="Value"
                    ),
                ),
                (
                    "value_float",
                    models.FloatField(blank=True, default=0.0, verbose_name="Value"),
                ),
                (
                    "value_image",
                    models.FileField(
                        blank=True, upload_to="images", verbose_name="Value"
                    ),
                ),
                (
                    "value_int",
                    models.IntegerField(blank=True, default=0, verbose_name="Value"),
                ),
                (
                    "value_string",
                    models.CharField(blank=True, max_length=50, verbose_name="Value"),
                ),
                (
                    "value_text",
                    models.TextField(blank=True, verbose_name="Value"),
                ),
                (
                    "value_time",
                    models.TimeField(blank=True, null=True, verbose_name="Value"),
                ),
                (
                    "value_url",
                    models.URLField(blank=True, verbose_name="Value"),
                ),
            ],
            options={
                "verbose_name": "Setting",
                "verbose_name_plural": "Settings",
                "ordering": ["name"],
            },
        ),
    ]
