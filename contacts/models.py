from django.db import models

class Contact(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="نام و نام خانوادگی"
    )
    
    mobile = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="تلفن همراه"
    )
    
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ تولد"
    )
    
    created_at = models.DateTimeField(
        auto_now=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.full_name
    
    
class ContactImage(models.Model):
    
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        related_name="image"
    )
    
    image_data = models.BinaryField(
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"Image of {self.contact.full_name}"