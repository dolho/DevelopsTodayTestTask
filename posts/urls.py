from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter
from posts import views


router = SimpleRouter()
router.register("posts", views.PostViewSet)

comments_router = NestedSimpleRouter(router, "posts", lookup="coments")
comments_router.register("comments", views.CommentViewSet, basename="post-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(comments_router.urls)),
]
