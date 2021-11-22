from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from .models import Article, Tag, Profile, Comment

class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class ArticleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("uuid", "display_name", "screen_name")


class TagSerializer(serializers.ModelSerializer):
    article_count = serializers.IntegerField(source='articles.count', read_only=True)
    class Meta:
        model = Tag
        fields = ("uuid", "name", "article_count")


class CommentSerializer(serializers.ModelSerializer):
    writer = ArticleProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ("uuid", "writer", "text", "article", "created_at")
        read_only_fields = ("created_at",)


class CommentWithArticleSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ("uuid", "writer", "text", "article", "created_at")
        read_only_fields = ("created_at", "article")


class ArticleSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(many=True, slug_field="name", queryset=Tag.objects.all())
    writer = ArticleProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    is_stocked = serializers.SerializerMethodField(read_only=True)

    def get_is_stocked(self, obj):
        try:
            profile = self.context['request'].user.stock_profile
        except KeyError:
            return None
        try:
            profile.stocks.get(pk=obj.pk)
            return True
        except Article.DoesNotExist:
            return False

    class Meta:
        model = Article
        fields = ("uuid", "title", "text", "writer", "tags", "created_at", "comments", "is_stocked")
        read_only_fields = ("created_at", "writer", "comments", "is_stocked")


class ProfileSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    used_tags = TagSerializer(many=True, read_only=True)
    display_name = serializers.CharField(allow_null=False, label="公開名")
    screen_name = serializers.CharField(allow_null=False, label="スクリーンネーム")
    stocks = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ("uuid", "display_name", "screen_name", "articles", "used_tags", "stocks")


class MyProfileSerializer(ProfileSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    is_iniad_member = serializers.BooleanField(source='user.is_iniad_member', read_only=True)
    is_student = serializers.BooleanField(source='user.is_student', read_only=True)
    is_authenticated = serializers.BooleanField(source='user.is_authenticated', read_only=True)

    class Meta:
        model = Profile
        fields = ("uuid", "display_name", "screen_name", "articles", "used_tags", "stocks", "email", "is_iniad_member", "is_student", "is_initialized", "is_authenticated")
        read_only_fields = ("is_initialized",)


class StockSerializer(serializers.Serializer):
    method = serializers.CharField(read_only=True)
    article = ArticleSerializer(many=True, read_only=True)

    class Meta:
        fields = ("method", "article")
        read_only_fields = ("method", "article")
