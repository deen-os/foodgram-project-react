from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import IngredientViewSet, TagViewSet, RecipeViewSet

app_name = 'recipes'

router = SimpleRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)

urlpatterns = [path('', include(router.urls))]
