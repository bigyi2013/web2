from django.urls import path

from . import views
app_name = 'log'
urlpatterns = [
    path('', views.log_page, name='log'),
    path('liuyan',views.liuyan,name='liuyan'),
    path('about',views.about,name='about'),
]