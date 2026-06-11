from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ContactForm

class ContactListView(ListView):
    
    model = Contact
    template_name= "contacts/contact_list.html"
    context_object_name= "contacts"

class ContactCreateView(CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy("contact-list")