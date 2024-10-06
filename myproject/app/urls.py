from django.urls import path

from . import views
urlpatterns = [
     path('upload/', views.ImageUploadView, name='image-upload'),
     path('register/',views.UserRegister,name='register-user'),
     path('login/',views.UserLogin,name='login-user'),
     path('logout/',views.custom_logout_view, name='logout'),
]