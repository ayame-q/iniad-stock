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
        fields = ("uuid", "writer", "text", "article")


class ArticleSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(many=True, slug_field="name", queryset=Tag.objects.all())
    writer = ArticleProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ("uuid", "title", "text", "writer", "tags", "created_at", "comments")
        read_only_fields = ("created_at", "writer", "comments")


class ProfileSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    class Meta:
        model = Profile
        fields = ("uuid", "display_name", "screen_name", "articles")
