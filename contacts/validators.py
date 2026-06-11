import re

from django.core.exceptions import ValidationError

def validate_mobile(value):
    
    pattern = r"^09\d{9}$"
    
    if not re.match(pattern, value):
        raise ValidationError(
            " شماره همراه باید 11 رقمی و معتبر باشد"
        )
    