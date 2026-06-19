from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Contact, ContactImage
from django.urls import reverse_lazy
from .forms import ContactForm, SearchForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages

class ContactListView(ListView):
    
    model = Contact
    template_name= "contacts/contact_list.html"
    context_object_name= "contacts"
    
    paginate_by = 5
    
    def get_queryset(self):
        
        queryset = Contact.objects.all()
        
        form = SearchForm(
            self.request.GET
        )
        
        if form.is_valid():
        
            query = form.cleaned_data.get("q")
            
            start_date = form.cleaned_data.get(
            "start_date"
            )
        
            end_date = form.cleaned_data.get(
                "end_date"
            )
            
            sort_by = form.cleaned_data.get(
                "sort_by"
            )
        
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
        
            if sort_by:
                queryset = queryset.order_by(sort_by)
            else:
                queryset = queryset.order_by("full_name")
        
            return queryset
    
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["search_form"] = SearchForm(
            self.request.GET
    )

        querydict = self.request.GET.copy()

        querydict.pop("page", None)

        context["query_string"] = querydict.urlencode()

        return context
    
    
            
            

class ContactCreateView(CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy("contact-list")
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        image_file = form.cleaned_data.get("image")
        
        if image_file:
            ContactImage.objects.create(
                contact=self.object,
                image_data=image_file.read()
            )
            
        messages.success(
            self.request,
            "مخاطب با موفقیت ثبت شد"
        )
        
        return response
    
class ContactUpdateView(UpdateView):
    
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contact_form.html"
    success_url = reverse_lazy("contact-list")
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        image_file = form.cleaned_data.get("image")
        
        if image_file:
            
            image_obj, created = ContactImage.objects.get_or_create(
                contact=self.object
            )
            
            image_obj.image_data = image_file.read()
            image_obj.save()
            
        messages.success(
            self.request,
            "اطلاعات مخاطب با موفقیت بروزرسانی شد"
        )
            
        return response
    
class ContactDeleteView(DeleteView):
    
    model = Contact
    template_name = "contacts/contact_confirm_delete.html"
    success_url = reverse_lazy("contact-list")
    
    def form_valid(self, form):
        
        messages.success(
            self.request,
            "مخاطب با موفقیت حذف شد"
        )
        return super().form_valid(form)
    
     
     
     
class ContactDetailView(DetailView):
    
    model = Contact
    
    template_name = "contacts/contact_detail.html"
    
    context_object_name = "contact"
     
def contact_image_view(request, pk):
    
    try:
        image = ContactImage.objects.get(
            contact_id=pk
        )
        
        return HttpResponse(
            image.image_data,
            content_type="image/jpeg"
        )
    except ContactImage.DoesNotExist:
        return HttpResponse(status=404)
    
    
    
