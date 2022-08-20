from django.urls import include, path

from .views import SubscriptionsView, SubcribeView

app_name = 'users'

urlpatterns = [
    path(
        'users/subscriptions/', SubscriptionsView.as_view(),
        name='subscriptions'
    ),
    path(
        'users/<int:pk>/subscribe/', SubcribeView.as_view(), name='subscribe'
    ),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
