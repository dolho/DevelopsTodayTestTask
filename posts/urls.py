from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter
from posts import views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r"posts", views.PostViewSet, basename="posts")
# router.register(r"posts/comments", views.PostViewSet, basename="comments")

router = SimpleRouter()
router.register(r"posts", views.PostViewSet)

comments_router = NestedSimpleRouter(router, r"posts", lookup="coments")
comments_router.register(r"comments", views.CommentViewSet, basename="post-comments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("", include(comments_router.urls)),
]
