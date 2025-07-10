from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeView, MenuByRoleView, LogoutView, RegisterView, UserListViewSet

router = DefaultRouter()
router.register(r"", UserListViewSet, basename="user")  # di-root `/api/users/`

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('menus/', MenuByRoleView.as_view(), name='menus-by-role'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
]
