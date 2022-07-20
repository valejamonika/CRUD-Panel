
from django.contrib import admin
from django.urls import path

from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('go', views.go),
    path('welcome', views.welcome),
    path('add', views.add),
    path('update',views.update),
    path('display',views.display),
    path('delete',views.delete),
    path('reguser',views.reguser),
    path('moredata',views.moredata),
    path('moreupdate',views.moreupdate),
    path('dele',views.dele),
    path('logout',views.logout),


]
