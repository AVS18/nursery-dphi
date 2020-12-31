from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addPlants',views.addPlants,name="addPlants"),
    path('viewOrder',views.viewOrder,name="viewOrder")
]