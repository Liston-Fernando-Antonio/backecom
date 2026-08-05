from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Client'),
        ('staff', 'Employé'),
        ('admin', 'Administrateur'),
        ('influencer', 'Influenceuse'),
    ]

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    reset_password_token = models.CharField(max_length=50, default="", blank=True)
    reset_password_expire = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Profile de {self.user.email} ({self.get_role_display()})"

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):

    user = instance

    if created:
        profile = Profile(user=user)
        profile.save()
    else:
        Profile.objects.get_or_create(user=user)
