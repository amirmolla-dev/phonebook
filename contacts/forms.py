from django import forms
from .models import Contact
from datetime import date

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
        
    def clean_birth_date(self):
        
        birth_date = self.cleaned_data.get("birth_date")
        
        if birth_date and birth_date > date.today():
            
            raise forms.ValidationError(
                "تاریخ نمی تونه در آینده باشه!"
            )
            
        return birth_date
    
    def clean_full_name(self):
        
        full_name = self.cleaned_data.get("full_name")
        
        if len(full_name.strip()) < 3:
            
            raise forms.ValidationError(
                "نام باید حداقل 3 کاراکتر باشه!"
            )
            
        return full_name