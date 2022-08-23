from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import SubscriptionsViewSet

app_name = 'users'

router = SimpleRouter()
router.register('users', SubscriptionsViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
