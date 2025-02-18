from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('aboutfdgdfsagdgd1/',views.about,name='aboutus'),
]

