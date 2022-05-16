from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.testview, name='home'),
    path('login/', views.loginView, name='login'),
    path('upload/', views.uploadCsvView, name='upload_csv'),
    path('content/', views.contentView, name='content'),
]
