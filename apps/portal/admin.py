from django.contrib import admin

# Register your models here.
from portal.models import News

#Blog模型的管理器
class NewsAdmin(admin.ModelAdmin):
    list_display=('id', 'title','content')
    list_display_links = ('id', 'title','content')

admin.site.register(News,NewsAdmin)
