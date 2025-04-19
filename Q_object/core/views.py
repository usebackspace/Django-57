from django.shortcuts import render
from .models import MarvelModel
from django.db.models import Q

# Create your views here.
def index(request):
    # mf=MarvelModel.objects.all()
    mf = MarvelModel.objects.filter(Q(city='NYC') & Q(name='Steve Roger'))
    mf = MarvelModel.objects.filter(Q(city='NYC') | Q(name='Steve Roger'))
    mf = MarvelModel.objects.filter(~Q(city='NYC'))

    return render(request,'core/index.html',{'mf':mf})