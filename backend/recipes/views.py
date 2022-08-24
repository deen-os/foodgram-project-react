import rest_framework.permissions
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import IngredientFilter, RecipeFilter, Recipe
from .models import Ingredient, Tag, Favorite, ShoppingCart, IngredientRecipe
from .permissions import IsAuthenticatedOwnerOrReadOnly
from .serializers import (
    IngredientSerializer, TagSerializer, RecipeSerializer,
    FollowRecipeSerializer
)
from .utils import download_pdf


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    pagination_class = None
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = (IngredientFilter,)
    search_fields = ('^name',)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    pagination_class = None
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @staticmethod
    def __favorite_shopping(request, pk, model, errors):
        if request.method == 'POST':
            if model.objects.filter(user=request.user, recipe__id=pk).exists():
                return Response(
                    {'errors': errors['recipe_in']},
                    status=status.HTTP_400_BAD_REQUEST
                )
            recipe = get_object_or_404(Recipe, id=pk)
            model.objects.create(user=request.user, recipe=recipe)
            serializer = FollowRecipeSerializer(
                recipe, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        recipe = model.objects.filter(user=request.user, recipe__id=pk)
        if recipe.exists():
            recipe.delete()
            return Response(
                {'msg': 'Успешно удалено'},
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {'error': errors['recipe_not_in']},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[rest_framework.permissions.IsAuthenticated]
    )
    def favorite(self, request, pk):
        return self.__favorite_shopping(request, pk, Favorite, {
            'recipe_in': 'Рецепт уже в избранном',
            'recipe_not_in': 'Рецепта нет в избранном'
        })

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=[rest_framework.permissions.IsAuthenticated]
    )
    def shopping_cart(self, request, pk):
        return self.__favorite_shopping(request, pk, ShoppingCart, {
            'recipe_in': 'Рецепт уже в списке покупок',
            'recipe_not_in': 'Рецепта нет в спике покупок'
        })

    @action(
        methods=['GET'],
        detail=False,
        permission_classes=[rest_framework.permissions.IsAuthenticated]
    )
    def download_shopping_cart(self, request):
        ingredients_obj = (
            IngredientRecipe.objects.filter(recipe__carts__user=request.user)
            .values('ingredient__name', 'ingredient__measurement_unit')
            .annotate(sum_amount=Sum('amount'))
        )
        data_dict = {}
        ingredients_list = []
        for item in ingredients_obj:
            name = item['ingredient__name'].capitalize()
            unit = item['ingredient__measurement_unit']
            sum_amount = item['sum_amount']
            data_dict[name] = [sum_amount, unit]
        for ind, (key, value) in enumerate(data_dict.items(), 1):
            if ind < 10:
                ind = '0' + str(ind)
            ingredients_list.append(
                f'{ind}. {key} - ' f'{value[0]} ' f'{value[1]}'
            )
        return download_pdf(ingredients_list)
