from rest_framework import viewsets
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer, UpvotesSerializer
from posts.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    """
    This endpoint allows to perfom CRUD operations over Posts
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

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
    permission_classes = [IsOwnerOrReadOnly]
