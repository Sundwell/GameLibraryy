from django.urls import path
from core.views import RegisterView, UserLoginView
from games.views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]

