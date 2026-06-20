from django import forms
from .models import Contact, ContactImage
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["birth_date"].widget.attrs.update(
        {
        "class": "form-control",
        "type": "date",
        }
        
        )
        
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control"
                }
            )
        
        
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
    
    
class SearchForm(forms.Form):
    
    q = forms.CharField(
        required=False
    )
    
    start_date = forms.DateField(
        required=False
    )
    
    end_date = forms.DateField(
        required=False
    )
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        start_date = cleaned_data.get("start_date")
        end_date   = cleaned_data.get("end_date")
        
        if ( start_date and end_date and start_date > end_date):
            
            raise forms.ValidationError(
                "نمیشه که تاریخ شروع بعد از تاریخ پایان باشه !"
            )
            
        return cleaned_data
    
    SORT_CHOICES = [
        ("full_name", "نام (الفبا)"),
        ("birth_date", "تاریخ تولد"),
        ("-created_at", "جدیدترین"),
        ("created_at", "قدیمی ترین"),
    ]
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False
    ) 
    