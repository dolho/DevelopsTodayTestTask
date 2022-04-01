from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="posts")
router.register(r"posts/comments", views.PostViewSet, basename="comments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
