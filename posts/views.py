from rest_framework import viewsets
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer, UpvotesSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        user = request.user.id
        serializer = UpvotesSerializer(data={"user": user, "post": pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "post upvoted"})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(parent_post=self.kwargs["posts_pk"])

    def create(self, request, *args, **kwargs):
        try:
            post = get_object_or_404(Post, pk=self.kwargs["posts_pk"])
        except Http404:
            return Response({"status": "not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(
            data={
                "content": request.data.get("content"),
            },
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(parent_post=post)
        return Response({"id": comment.id, "content": comment.content})
