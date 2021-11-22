import sys
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.models import Count
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from . import models, serializers


# Create your views here.
class ArticleViewSet(ModelViewSet):
    queryset = models.Article.objects.order_by("-created_at")
    serializer_class = serializers.ArticleSerializer

    @action(detail=False)
    def trends(self, request, *args, **kwargs):
        self.queryset = models.Article.objects.order_by("-created_at")
        return super(ArticleViewSet, self).list(self, request, *args, **kwargs)

    @action(detail=False)
    def recents(self, request, *args, **kwargs):
        self.queryset = models.Article.objects.order_by("-created_at")
        return super(ArticleViewSet, self).list(self, request, *args, **kwargs)

    @action(detail=False)
    def recently_comments(self, request, *args, **kwargs):
        self.queryset = models.Article.objects.order_by("-comments__created_at").distinct("uuid")
        return super(ArticleViewSet, self).list(self, request, *args, **kwargs)

    @action(detail=True, methods=["POST", "DELETE"])
    def stock(self, request, pk=None):
        method_to_str = {"POST": "add", "DELETE": "remove"}
        article = get_object_or_404(models.Article, pk=pk)
        if request.method == "POST":
            request.user.stock_profile.stocks.add(article)
        elif request.method == "DELETE":
            request.user.stock_profile.stocks.remove(article)
        serializer = serializers.ArticleSerializer(instance=article, context={"request": request})
        return Response({"method": method_to_str[request.method], "article": serializer.data})

    def perform_create(self, serializer):
        try:
            serializer.save(writer=self.request.user.stock_profile)
        except DjangoValidationError as e:
            print(e.message, file=sys.stderr)
            raise ValidationError(e.message)

    def perform_update(self, serializer):
        if serializer.instance.writer.user != self.request.user:
            raise PermissionDenied("他人の記事を編集することはできません")
        super(ArticleViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.writer.user != self.request.user:
            raise PermissionDenied("他人の記事を削除することはできません")
        super(ArticleViewSet, self).perform_destroy(instance)


class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        article_pk = self.kwargs.get("article_uuid")
        if article_pk:
            return serializers.CommentWithArticleSerializer
        return serializers.CommentSerializer

    def get_queryset(self):
        article_pk = self.kwargs.get("article_uuid")
        return models.Comment.objects.filter(article_id=article_pk)

    def perform_create(self, serializer):
        try:
            article_pk = self.kwargs.get("article_uuid")
            if article_pk:
                serializer.save(writer=self.request.user.stock_profile, article_id=article_pk)
            serializer.save(writer=self.request.user.stock_profile)
        except DjangoValidationError as e:
            print(e.message, file=sys.stderr)
            raise ValidationError(e.message)


class ProfileViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("他人のプロフィールを編集することはできません")
        super(ProfileViewSet, self).perform_update(serializer)


class MyUserAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.MyProfileSerializer

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({
                "is_authenticated": False,
                "uuid": None,
                "display_name": None,
                "screen_name": None,
                "articles": [],
                "is_initialized": False,
            })
        return super(MyUserAPIView, self).get(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.stock_profile

    def perform_update(self, serializer):
        serializer.save(is_initialized=True)


class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.annotate(article_count=Count('articles')).order_by('-article_count')
    serializer_class = serializers.TagSerializer
