from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home,name="home"),
    path('<str:category>/',views.search,name="search"),
    path('view/<str:id>',views.view,name="view")
]