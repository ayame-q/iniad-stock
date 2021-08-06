import sys
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.models import Count
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from . import models, serializers


# Create your views here.
class ArticleViewSet(ModelViewSet):
    queryset = models.Article.objects.order_by("-created_at")
    serializer_class = serializers.ArticleSerializer

    @action(detail=False)
    def trends(self, request, *args, **kwargs):
        self.queryset = models.Article.objects.order_by("created_at")
        return super(ArticleViewSet, self).list(self, request, *args, **kwargs)

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


class ProfileViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("他人のプロフィールを編集することはできません")
        super(ProfileViewSet, self).perform_update(serializer)


class MyUserAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        return self.request.user.stock_profile


class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.annotate(article_count=Count('articles')).order_by('-article_count')
    serializer_class = serializers.TagSerializer
