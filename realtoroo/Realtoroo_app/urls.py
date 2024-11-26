from django.urls import path
from . import views
urlpatterns = [
 path('',views.sign_up,name='sign_up'),
 path('login/',views.login,name='login'),
 path('Register_pro/',views.Registerprocess),
 path('login_pro/',views.loginprocess),
 path('houses/',views.houses,name='houses'),
 path('view_details/', views.details),
 path('register_house/', views.register_house, name='register_house'),
]