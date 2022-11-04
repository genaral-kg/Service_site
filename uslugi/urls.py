from django.urls import path, include

from .views import UslugiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service', UslugiViewSet)

urlpatterns = [
    path('', include(router.urls))
]