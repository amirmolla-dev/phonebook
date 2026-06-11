from django.urls import path

from .views import (
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
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
]
