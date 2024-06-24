from django.db import models



class Work(models.Model):
    id = models.AutoField(
        serialize=True,
        auto_created=True,
        primary_key=True,
        verbose_name = 'ID',
        null=False,
        blank=False,
    )

    name = models.CharField(
        primary_key=False,
        max_length=128,
        verbose_name = '作品タイトル',
        null=False,
        blank=False,
    )

    production_period = models.DateField(
        primary_key=False,
        verbose_name = '制作期間',
        null=False,
        blank=False,
    )

    project_url = models.TextField(
        primary_key=False,
        verbose_name="作品URL",
        null=True,
        blank=True,
    )

    description = models.TextField(
        primary_key=False,
        verbose_name="作品説明",
        null=False,
        blank=False,
    )


class Image(models.Model):
    id = models.AutoField(
        serialize=True,
        auto_created=True,
        primary_key=True,
        verbose_name="ID",
        null=False,
        blank=False,
    )

    Work_id = models.IntegerField(
        auto_created=True,
        primary_key=True,
        verbose_name="作品ID",
        null=False,
        blank=False,
    )
    image_path = models.TextField(
        primary_key=False,
        verbose_name="画像URL",
        null=False,
        blank=False,
    )

class UsedLang(models.Model):
    work_id = models.IntegerField(
        auto_created=True,
        primary_key=True,
        verbose_name="作品ID",
        null=False,
        blank=False,
    )
    language_id = models.IntegerField(
        primary_key=True,
        verbose_name="言語ID",
        null=False,
        blank=False,
    )

class Languge(models.Model):
    id = models.AutoField(
        serialize=True,
        primary_key=True,
        verbose_name='ID',
        null=False,
    )

    name = models.CharField(
        verbose_name = '言語名',
        max_length=64,
        primary_key=False,
        null=False
    )
# Create your models here.
