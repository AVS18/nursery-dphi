from django.urls import path,include
from .views import UserViewSet,OrderViewSet,PlantViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet,basename='user List')
router.register(r'order', OrderViewSet,basename='order List')
router.register(r'plants', PlantViewSet,basename='plant List')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
