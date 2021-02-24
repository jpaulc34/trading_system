from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views.views import *

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"stocks", StockViewSet)
router.register(r"orders", OrderViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update"),
    path("orders/<int:user_profile_pk>/user/",OrderGetCreateView.as_view(), name="user_profile-order"),
]
 