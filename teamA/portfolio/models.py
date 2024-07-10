from django.db import models



class Work(models.Model):
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

    project_url = models.URLField(
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

    work_id = models.ForeignKey(
        Work, on_delete=models.CASCADE,
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
class Language(models.Model):

    name = models.CharField(
        verbose_name = '言語名',
        max_length=64,
        primary_key=False,
        null=False
    )
# Create your models here.

class UsedLang(models.Model):
    work_id = models.ForeignKey(
        Work, on_delete=models.CASCADE,
        verbose_name="作品ID",
        null=False,
        blank=False,
    )
    language_id = models.ForeignKey(
        Language, on_delete=models.CASCADE,
        verbose_name="言語ID",
        null=False,
        blank=False,
    )

