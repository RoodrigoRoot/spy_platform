from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    """
    Custom authentication to login a user with a email and password
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = UserModel.objects.get(email__iexact=username)
        if not user:
            return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user