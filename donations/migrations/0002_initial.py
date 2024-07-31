# Generated by Django 5.0 on 2024-07-30 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("donations", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="basket",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="basket_item",
            name="basket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="donations.basket",
            ),
        ),
        migrations.AddField(
            model_name="cheering",
            name="basket_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="donations.basket",
                verbose_name="꿈바구니 고유번호",
            ),
        ),
        migrations.AddField(
            model_name="cheering",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="회원 아이디",
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="basket_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="donations.basket",
                verbose_name="꿈바구니 고유번호",
            ),
        ),
        migrations.AddField(
            model_name="donation",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="회원 아이디",
            ),
        ),
        migrations.AddField(
            model_name="donation_item",
            name="basket_item_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="donations.basket_item",
                verbose_name="꿈바구니 물품",
            ),
        ),
        migrations.AddField(
            model_name="donation_item",
            name="donation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donation_items",
                to="donations.donation",
                verbose_name="기부드림 고유번호",
            ),
        ),
        migrations.AddField(
            model_name="basket_item",
            name="goods",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="donations.goods",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="donation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="donations.donation",
                verbose_name="기부드림 고유번호",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="회원 아이디",
            ),
        ),
    ]
