from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('about/',views.about,name='aboutus'),
    # path('about/<str>/',views.about1,name='aboutus'),
    path('about/<int:id>/',views.about1,name='aboutus'),
]

