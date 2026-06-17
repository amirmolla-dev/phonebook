from django.urls import path

from .views import (
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    contact_image_view,
)

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
    
    path(
        "edit/<int:pk>/",
        ContactUpdateView.as_view(),
        name="contact-edit"
    ),
    
    path(
        "delete/<int:pk>/",
        ContactDeleteView.as_view(),
        name="contact-delete"
    ),
    
    path(
        "image/<int:pk>/",
        contact_image_view,
        name="contact-image"
    ),
]
