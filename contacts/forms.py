from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    image = forms.ImageField(
        required=False,
        label = "تصویر"
    )
    class Meta:
        
        model = Contact
        fields = [
            "full_name",
            "mobile",
            "birth_date",
        ]