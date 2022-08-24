from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import SubscriptionsViewSet, SubscriptionsView

app_name = 'users'

router = SimpleRouter()
router.register('users', SubscriptionsViewSet, basename='user')

urlpatterns = [
    path(
            'users/subscriptions/', SubscriptionsView.as_view(),
            name='subscriptions'
        ),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
