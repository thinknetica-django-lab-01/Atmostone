from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('<pk>', views.ProfileUpdate.as_view(), name='profile'),
    path('login/', views.login, name='login'),
]