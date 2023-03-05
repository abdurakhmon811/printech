"""Defines assisting functions or classes for either view functions or anything else."""
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.shortcuts import get_list_or_404
from phonenumber_field.validators import validate_international_phonenumber

import re

class AuthenticationValidator:
    """
    An assisting class.

    Validates the authentication form, either registration, login with username or login with phone_number.
    """

    def __init__(self):
        
        self.checkpattern
        self.validate_name
        self.validate_password
        self.validate_phone_number
        self.validate_username
    
    def checkpattern(self, pattern, value: str) -> bool:
        """
        An assisting function.

        Checks whether the passed string contains the pattern or not.

        :param pattern: Takes in regular expressions as a raw string.
        :param value: Takes in a value to be checked.
        :return: A boolean value based on the test result.
        """

        pat = re.compile(pattern)
        
        return True if pat.search(value) is not None else False
    
    def validate_name(self, value: str, middle_name=False) -> bool:
        """
        An assisting function.

        Validates the posted name (can be any name) based on regular expressions.

        :param value: Takes in a name as a string.
        :return: A boolean value based on the test result.
        """

        hassymbols = self.checkpattern(r"[^a-zA-Z'`]", value)

        if not middle_name:
            return True if not hassymbols and not isempty(value) else False
        else:
            return True if not hassymbols else False


    def validate_password(self, value: str) -> bool:
        """
        An assisting function.

        Validates the posted password.

        :param value: Takes in a string of the password.
        :return: A boolean value based on the test result.
        """

        # NOTE: Checks should be made based on what passwords should and should not contain, that is:
            # Includes:
                # 1. Digits
                # 2. Uppercase letters
                # 3. 8 characters at least
            # Excludes:
                # 1. Certain symbols
        # NOTE: Also check whether a password is not empty

        hasdigit = self.checkpattern(r'\d', value)
        hasuppercase = self.checkpattern(r'[A-Z]', value)
        length_valid = True if len(value) > 8 else False

        hassymbols = self.checkpattern(r'[!%^&*()-+:;\/]', value)

        return True if hasdigit and hasuppercase and length_valid and not hassymbols and not isempty(value) else False


    def validate_phone_number(self, value: str) -> bool:
        """
        An assisting function.

        Validates the posted phone number based on the region defined in the settings.

        :param value: Takes in a string containing the phone number.
        :return: A boolean value based on the test result.
        """

        invalid = None

        try:
            validate_international_phonenumber(value)
        except ValidationError:
            invalid = True
        else:
            invalid = False

        empty = True if value is None or value == '' or value == '+998' else False

        return True if invalid == False and empty == False else False


    def validate_user_id(self, value) -> bool:
        """
        An assisting function.

        Validates the user id based on regular expressions.
        :param value: Takes in a string of user id.
        :return: A boolean value based on the test result.
        """

        converted_value = str(value)

        invalid = self.checkpattern(r'[^a-zA-Z0-9_]', converted_value)

        return True if not invalid and not isempty(converted_value) else False


    def validate_username(self, value: str) -> bool:
        """
        An assisting function.

        Validates the posted username based on regular expressions.

        :param value: Takes in a string of the username.
        :return: A boolean value based on the test result.
        """

        # Checks whether the username does not have any other characters than lower and upper case letters, 
        # digits and an underscore
        hassymbols = self.checkpattern(r'[^a-zA-Z0-9_]', value)
        length_valid = True if len(value) > 5 and len(value) < 30 else False

        return True if not hassymbols and length_valid and not isempty(value) else False


def isempty(value: str) -> bool:
    """
    An assisting function.

    Checks whether the passed value is empty or None.

    :return: A boolean value based on the test result.
    """

    return True if value is None or value == '' else False


def phone_number_exists(obj: str, queryset) -> bool:
    """
    An assisting function.

    Determines whether the provided phone number exists in the provided queryset of users.

    :param obj: Takes in a value (string).
    :param queryset: Takes in the table of the CustomUser or User model.
    """

    result = None
    for each in queryset:
        if str(obj) == each.phone_number:
            result = True
            break
        else:
            result = False

    return result


def username_exists(obj: str, queryset) -> bool:
    """
    An assisting function.

    Determines whether the provided username exists in the provided queryset of users.

    :param obj: Takes in a value (string).
    :param queryset: Takes in the table of the CustomUser or User model.
    """

    
