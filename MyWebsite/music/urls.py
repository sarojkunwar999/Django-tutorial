from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/71
    path('<int:album_id>/', views.detail, name='detail'),

]
