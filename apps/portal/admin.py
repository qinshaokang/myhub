from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from portal.models import News, Introduction, Speech, ContactUs, Product


#新闻的管理器
class NewsAdmin(admin.ModelAdmin):
    list_display=('id', 'title','content')
    list_display_links = ('id', 'title','content')

class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('id','title','content')
    list_display_links = ('id','title','content')

class SpeechAdmin(admin.ModelAdmin):
    list_display = ('id','title','content')
    list_display_links = ('id','title','content')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','title','telephone','qq','wechat','email','address')
    list_display_links = ('id','title','telephone','qq','wechat','email','address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','discription','image_data')
    list_display_links = ('id','name','discription')
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.picture.url)

    image_data.short_description = u'品牌图片'

admin.site.register(News,NewsAdmin)
admin.site.register(Introduction,NewsAdmin)
admin.site.register(Speech,SpeechAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(Product,ProductAdmin)
