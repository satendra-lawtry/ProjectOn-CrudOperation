
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('show/',views.showRecord),
    path('delete/<int:id>',views.deleteRecord),
    path('edit/<int:id>',views.editdata),
    path('changedata/',views.changeData)
]
