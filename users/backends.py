from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404
from .assistants import *
from .models import CustomUser


class CustomBackend(BaseBackend):
    """
    A custom backend that authenticates or gets a user.
    """

    def __init__(self):

        super().__init__()

        self.validator = AuthenticationValidator()

    def authenticate(self, request: HttpRequest, username=None, phone_number=None, password=None):
        """
        Authenticate the request user by username (or telephone number) and password.
        """

        if phone_number is None and username is not None and password is not None:
            username_safe = self.validator.validate_username(username)
            password_safe = self.validator.validate_password(password)
            if username_safe and password_safe:
                try:
                    user = get_object_or_404(CustomUser, username=username, password=password)
                except Http404:
                    return None
                else:
                    return user
        elif username is None and phone_number is not None and password is not None:
            phone_number_safe = self.validator.validate_phone_number(phone_number)
            password_safe = self.validator.validate_password(password)
            if phone_number_safe and password_safe:
                try:
                    user = get_object_or_404(CustomUser, phone_number=phone_number, password=password)
                except Http404:
                    return None
                else:
                    return user
        else:
            return None

    def get_user(self, user_id):
        """
        Get the user with the passed user id if it exists else return None.
        """

        id_valid = self.validator.validate_user_id(user_id)

        if id_valid:
            try:
                user = get_object_or_404(CustomUser, pk=user_id)
            except Http404:
                return None
            else:
                return user
