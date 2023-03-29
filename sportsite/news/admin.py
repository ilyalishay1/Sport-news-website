from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'is_published', 'date', 'category')
    list_display_links = ('title',)
    search_fields = ('title', 'content')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
admin.site.register(FootballCategory)
admin.site.register(BasketballCategory)
admin.site.register(HockeyCategory)
