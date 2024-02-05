from django.core.exceptions import ValidationError
import re

def validate_name(name):
    error_messasge = "Improper name"
    regex = r'[a-zA-Z0-9\s]+$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_messasge, params={"name" : name})