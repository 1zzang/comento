from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import MainContents

def index(request):
    content_list = MainContents.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(request, 'product/content_list.html',context)