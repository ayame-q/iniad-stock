from django.contrib import admin
from .models import Article, Comment, Profile, Tag

# Register your models here.
class UUIDFieldAdmin(admin.ModelAdmin):
    readonly_fields=('uuid',)

admin.site.register(Article, UUIDFieldAdmin)
admin.site.register(Profile, UUIDFieldAdmin)
admin.site.register(Tag, UUIDFieldAdmin)
admin.site.register(Comment, UUIDFieldAdmin)