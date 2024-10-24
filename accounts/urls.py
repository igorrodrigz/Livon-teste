from django.urls import path
from .views import SignUpView, LoginView, UserListView, UserDetailView, home, menu

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('menu/', menu, name='menu'),
]
