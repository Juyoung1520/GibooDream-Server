# Generated by Django 5.0 on 2024-08-02 08:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("nickname", models.CharField(max_length=30, unique=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("individual", "Individual"),
                            ("company", "Company"),
                            ("foreigner", "Foreigner"),
                        ],
                        default="individual",
                        max_length=10,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("terms1", models.BooleanField(default=False)),
                ("terms2", models.BooleanField(default=False)),
                ("terms3", models.BooleanField(default=False)),
                ("terms4", models.BooleanField(blank=True, default=False)),
                ("terms5", models.BooleanField(blank=True, default=False)),
                (
                    "donate_total",
                    models.IntegerField(default=0, verbose_name="총 기부 금액"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="BeneficiaryApplication",
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
                ("full_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                (
                    "detailed_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("contact_number", models.CharField(max_length=20)),
                ("id_number", models.CharField(max_length=20)),
                ("proof_document", models.FileField(upload_to="proof_documents/")),
                ("consent", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
