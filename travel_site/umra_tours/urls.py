from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UmraTourViewSet

router = DefaultRouter()
router.register(r'umra_tours', UmraTourViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
