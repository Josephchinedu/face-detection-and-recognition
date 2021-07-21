from django.contrib.auth.backends import ModelBackend
from .models import Records

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, request, first_name=None):
        try:
            return Records.objects.get(first_name=first_name)
        except Records.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Records.objects.get(pk=user_id)
        except Records.DoesNotExist:
            return None