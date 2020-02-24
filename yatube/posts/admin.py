from django.contrib import admin

from .models import Post, Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    empty_value_display = '-пусто-'

class PostAdmin(admin.ModelAdmin):
    # добавим в начало столбец pk
    list_display = ("pk", "text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = '-пусто-'

# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)