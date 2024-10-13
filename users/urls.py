from django.urls import path,include
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter

from .views import register,LoginView,CustomUserViewSet


router=DefaultRouter()

router.register(r'profile',CustomUserViewSet)

urlpatterns=[
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("",LoginView.as_view(),name="login"),
    path("accounts/",include(router.urls))

]