from django.urls import path
from . import views

urlpatterns=[
    path('list/',views.get,name="list"),
    path('list/<str:pk>',views.getId,name="listId"),
    path('login/',views.login,name="login"),
    path('add/',views.post,name="add"),
    path('update/',views.update,name="update"),
]