from django.urls import path
from .views import MeView, MenuByRoleView, LogoutView

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('menus/', MenuByRoleView.as_view(), name='menus-by-role'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
