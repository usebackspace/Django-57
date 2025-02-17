from django.shortcuts import render

# Create your views here.
def vilian(request):
    # context={'villian':'zola'}
    return render(request,'core/index.html',{'villian':'redskull'})


def hero(request):
    return render(request,'core/hero.html',{'hero':['captain america','ironman','spiderman','thor','black panther','black widow','hulk']})