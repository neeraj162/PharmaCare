from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('update/',views.update,name="update"),
    path('order/',views.order,name="order"),
    path('getmedicine/',views.getmedicine,name="getmedicine"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('signup/',views.signup,name="signup"),
    path("Logout/",views.Logout,name="Logout"),
]