from django.urls import path , include
from . import views
from rest_framework import routers


# urlpatterns = [
#     path('user',views.UserViewSet.as_view({'get': 'list'})),
#     path('login',views.UserViewSet.as_view({'post':"login"}))
# ]
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),

]

