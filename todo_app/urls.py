from . import views
from django.urls import path


urlpatterns=[
    path('',views.home,name='home'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:taskid>',views.update,name='update')


]