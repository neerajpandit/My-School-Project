from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexs, name='home'),
    path('student10/', views.student10, name='student10'),
    path('student12/', views.student12, name='student12'),
    path('passout/',views.passout, name="passout"),
    ]