# Generated by Django 5.0 on 2024-07-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Basket",
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
                ("buy_num", models.IntegerField(default=0, verbose_name="구매갯수")),
                (
                    "buy_reason",
                    models.CharField(default="", max_length=300, verbose_name="구매 이유"),
                ),
                (
                    "basket_post",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="꿈바구니 등록 날짜"
                    ),
                ),
                (
                    "basket_complete",
                    models.DateField(null=True, verbose_name="꿈바구니 완료 날짜"),
                ),
                (
                    "complete",
                    models.BooleanField(default=False, verbose_name="후원 완료 여부"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Basket_Item",
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
                ("buy_num", models.IntegerField(default=0, verbose_name="물품 수량")),
                ("price", models.IntegerField(default=0, verbose_name="총 가격")),
            ],
        ),
        migrations.CreateModel(
            name="Cheering",
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
                    "cheering_cont",
                    models.CharField(max_length=30, verbose_name="응원 문구"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Donation",
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
                ("goods_total_price", models.IntegerField(verbose_name="물품 총 가격")),
                (
                    "buy_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="구매 일자"),
                ),
                ("payment", models.CharField(max_length=100, verbose_name="결제 방법")),
                (
                    "receipt_yn",
                    models.BooleanField(default=False, verbose_name="영수증 발급 여부"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Donation_Item",
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
                ("quantity", models.IntegerField(verbose_name="물품 수량")),
            ],
        ),
        migrations.CreateModel(
            name="Goods",
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
                ("goods_price", models.IntegerField(verbose_name="물품 가격")),
                ("goods_name", models.CharField(max_length=40, verbose_name="물품 이름")),
                ("goods_num", models.IntegerField(verbose_name="물품 재고")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("review_cont", models.CharField(max_length=300, verbose_name="후기 내용")),
                ("review_img", models.ImageField(upload_to="", verbose_name="후기 이미지")),
            ],
        ),
    ]
