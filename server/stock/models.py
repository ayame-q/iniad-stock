from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="UUID")

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), related_name="stock_profile", null=True, on_delete=models.SET_NULL, verbose_name="ユーザー")
    display_name = models.CharField(max_length=20, null=True, verbose_name="公開名")
    screen_name = models.CharField(max_length=12, unique=True, null=True, verbose_name="スクリーンネーム")
    is_initialized = models.BooleanField(default=False, verbose_name="初期登録済み")
    created_at = models.DateTimeField(default=timezone.localtime, verbose_name="作成日")
    stocks = models.ManyToManyField("Article", related_name="stocked_users", verbose_name="ストック記事")

    def used_tags(self):
        return Tag.objects.filter(articles__in=self.articles.all()).distinct()


class Tag(BaseModel):
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name="名前")


class Article(BaseModel):
    title = models.CharField(max_length=30, verbose_name="タイトル")
    text = models.TextField(verbose_name="本文")
    writer = models.ForeignKey(Profile, related_name="articles", on_delete=models.PROTECT, verbose_name="筆者")
    tags = models.ManyToManyField(Tag, related_name="articles", verbose_name="タグ")
    created_at = models.DateTimeField(default=timezone.localtime, verbose_name="作成日")


class Comment(BaseModel):
    text = models.TextField(verbose_name="本文")
    writer = models.ForeignKey(Profile, related_name="comments", on_delete=models.PROTECT, verbose_name="筆者")
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE, verbose_name="記事")
    created_at = models.DateTimeField(default=timezone.localtime, verbose_name="作成日")

    class Meta:
        ordering = ("-created_at", )
