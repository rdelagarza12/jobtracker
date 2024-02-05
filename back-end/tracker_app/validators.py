from django.core.exceptions import ValidationError
import re

def validate_tracker_name(tracker_name):
    error_message = "Improper tracker name"
    regex = r'[a-zA-Z0-9\s]+$'
    good_name = re.match(regex, tracker_name)
    if good_name:
        return tracker_name
    else:
        raise ValidationError(error_message, params={'tracker_name' : tracker_name})
