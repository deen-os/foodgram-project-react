from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include('users.urls', namespace='users')),
        path('', include('recipes.urls', namespace='recipes'))
                 ]))
]
