from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Contact
from django.urls import reverse_lazy
from .forms import ContactForm
from django.db.models import Q

class ContactListView(ListView):
    
    model = Contact
    template_name= "contacts/contact_list.html"
    context_object_name= "contacts"
    
    def get_queryset(self):
        
        queryset = Contact.objects.all()
        
        query      = self.request.GET.get("q")
        start_date = self.request.GET.get("start_date")
        end_date   = self.request.GET.get("end_date")
        
        if query:
            
            queryset = queryset.filter(
                Q(full_name__icontains=query)
                |
                Q(mobile__icontains=query)
                
            )
            
        if start_date:
            queryset = queryset.filter(
                birth_date__gte=start_date
            )
        
        if end_date:
            queryset = queryset.filter(
                birth_date__lte=end_date
            )
        
        return queryset.order_by("full_name")
            
            

class ContactCreateView(CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy("contact-list")
    
class ContactUpdateView(UpdateView):
    
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contact_form.html"
    success_url = reverse_lazy("contact-list")
    
class ContactDeleteView(DeleteView):
    
    model = Contact
    template_name = "contacts/contact_confirm_delete.html"
    success_url = reverse_lazy("contact-list")
     
     
