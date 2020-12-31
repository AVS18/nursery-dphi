from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('viewPlant',views.viewPlant,name="viewPlant"),
    path('order',views.order,name="order"),
    path('addCart/<int:pid>',views.addCart,name="addCart"),
    path('viewCart',views.viewCart,name="viewCart"),
    path('removeItem/<int:pid>',views.removeItem,name="removeItem")
]