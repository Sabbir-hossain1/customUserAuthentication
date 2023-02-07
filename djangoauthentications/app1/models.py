from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self,email,user_name,first_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError("Super user must be assigned to is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Super user must be assigned to is_superuser=True. ")
        
        return self.create_superuser(email,user_name,first_name,password,**other_fields)
    
    def create_user(self,email,user_name,first_name,password,**other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
            

class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(("Email : "), max_length=254,unique=True)
    user_name = models.CharField(("User Name"), max_length=50,unique=True)
    first_name = models.CharField(("First Name: "), max_length=50,blank=True)
    start_date = models.DateField(("Start Date: "), auto_now_add=True)
    about = models.TextField(("About: "),blank=True)
    is_staff = models.BooleanField(("Is Staff ?"),default=False)
    is_active = models.BooleanField(("Active Status"),default=False)    
        
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']
    
    def __str__(self):
        return self.user_name