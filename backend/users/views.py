from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import User, Follow
from .serializers import FollowSerializer, UserSerializer


class SubscriptionsView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(following__user=user)


class SubcribeView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_class = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, pk):
        user = request.user
        author = get_object_or_404(User, id=pk)
        if author == user:
            return Response(
                {'error': 'Вы не можете подписаться на себя'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if Follow.objects.filter(user=user, author=author).exists():
            return Response(
                {'error': 'Повторная подписка недопустима'},
                status=status.HTTP_400_BAD_REQUEST
            )
        Follow.objects.create(user=user, author=author)
        follow = User.objects.filter(username=author).first()
        serializer = FollowSerializer(follow, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = request.user
        author = get_object_or_404(User, id=pk)
        if author == user:
            return Response(
                {'error': 'Нельзя отписаться от себя'},
                status=status.HTTP_400_BAD_REQUEST
            )
        follow = Follow.objects.filter(user=user, author=author)
        if follow.exists():
            follow.delete()
            return Response(
                {'msg': 'Вы успешно отписались'},
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {'error': 'Вы не подписаны на данного автора'},
            status=status.HTTP_400_BAD_REQUEST
        )
