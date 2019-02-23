from django.urls import path
from django.contrib.auth.views import (
    login,
    logout,
)

# Same app
from user_auth.views import (
    sign_up,
    profile,
    profile_create,
    profile_detail,
    profile_edit,
)


urlpatterns = [

    path('signup/', sign_up, name='signup'),
    path('login/', login, {'template_name': 'user_auth/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'home.html'}, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile-create/', profile_create, name='profile-create'),
    path('profile-detail/<int:id>/', profile_detail, name='profile-detail'),
    path('profile-edit/', profile_edit, name='profile-edit'),


]

