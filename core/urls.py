from django.urls import path
from core.views import RegisterView, UserLoginView, CustomLogoutView
from games.views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]

