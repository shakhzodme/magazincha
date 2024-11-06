from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import  WeatherAPI, TovarViewSet

router = DefaultRouter()
router.register("tovarlar", TovarViewSet)

urlpatterns = [
    # path("sync/", SyncAPI.as_view()),
    # path("", TovarlarAPI.as_view()),
    # path("<int:pk>/", TovarAPI.as_view()),
    path("obhavo/", WeatherAPI.as_view()),
    # path("token/", TokenForUser.as_view()),
] + router.urls