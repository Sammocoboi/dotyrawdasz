from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CarViews,FirmViews

router = DefaultRouter()
router.register(r'car',CarViews)
router.register(r'firm',FirmViews)

urlpatterns = [
    path('',include(router.urls)),
]

