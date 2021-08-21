from django.urls import path, register_converter
from users.views import home, register, profile_view, Profile_edit, ProfileUpdate
from django.contrib.auth import views as auth_view
from .utils import HashIdConverter

register_converter(HashIdConverter, "hashid")
urlpatterns = [
    path('', home, name="'home"),
    path('home/', home, name="home"),
    path('register/', register, name="register"),
    path('profile/', profile_view, name="profile"),
    path('profile_form/', Profile_edit, name='profile_edit'),
    path('profile_update/<hashid:pk>/',
         ProfileUpdate.as_view(), name='profile_update'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
]
