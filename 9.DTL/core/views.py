from django.shortcuts import render

# Create your views here.
def vilian(request):
    # context={'villian':'zola'}
    return render(request,'core/villian.html',{'villian':'vickyy'})


def hero(request):
    context ={'hero':['captain america','ironman','spiderman','thor','black panther','black widow','hulk']}
    return render(request,'core/hero.html',context)