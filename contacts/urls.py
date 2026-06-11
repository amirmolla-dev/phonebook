from django.urls import path

from .views import ContactListView, ContactCreateView

urlpatterns = [
    path(
        "",
        ContactListView.as_view(),
        name="contact-list"
    ),
    
    path(
        "create/",
        ContactCreateView.as_view(),
        name='contact-create'
    ),
]
