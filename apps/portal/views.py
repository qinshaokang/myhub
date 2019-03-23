from django.shortcuts import render

from portal.models import News, Introduction, Speech, ContactUs, Product


def index(request):
    news_list = News.objects.all().order_by('-create_time')[0:5]
    introduction = Introduction.objects.all().first()
    speech = Speech.objects.first()
    contactus = ContactUs.objects.first()
    product_list = Product.objects.all()[0:4]
    return render(request, 'portal/index.html',{'news_list':news_list,
                                                'introduction':introduction,
                                                'speech':speech,
                                                'contactus':contactus,
                                                'product_list':product_list} )

