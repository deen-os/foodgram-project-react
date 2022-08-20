from django.contrib import admin

from recipes.models import (
    Ingredient, Recipe, Tag, IngredientRecipe, ShoppingCart, Favorite
)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'color')
    list_editable = ('color',)
    list_display_links = ('name',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name', )
    list_display_links = ('name',)
    search_fields = ('name', )
    empty_value_display = '-пусто-'


class ReciptIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'author', 'text', 'cooking_time', 'pub_date', 'image',
                    )
    list_filter = ('name', 'author', 'tags')
    ordering = ('-pub_date',)
    inline = (ReciptIngredientInline, )
    readonly_fields = ('favorite_count', 'pub_date')
    list_display_links = ('name',)
    search_fields = ('name',)

    @admin.display(description='Добавлен в избранное')
    def favorite_count(self, recipe):
        return recipe.favorites_recipe.count()


class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    list_display_links = ('recipe',)
    search_fields = ('recipe',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    list_display_links = ('user',)
    search_fields = ('user',)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    list_display_links = ('user',)
    search_fields = ('user',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
