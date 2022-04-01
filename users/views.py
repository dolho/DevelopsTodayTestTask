from django.contrib.auth.models import User
from users.serializers import RegisterSerializer
from rest_framework import viewsets, permissions, mixins


class RegisterView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
