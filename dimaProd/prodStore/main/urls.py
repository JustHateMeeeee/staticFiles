from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('man', views.man),
    path('woman', views.woman),
    path('child', views.child),
    path('basket', views.basket)
]