from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import IngredientViewSet, TagViewSet, RecipeViewSet

app_name = 'recipes'

router = SimpleRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [path('', include(router.urls))]
