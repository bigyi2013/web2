from django.urls import path

from . import views
app_name = 'log'
urlpatterns = [
    path('', views.log_page, name='log'),
    path('comment',views.comment,name='comment'),
    path('about',views.about,name='about'),
]