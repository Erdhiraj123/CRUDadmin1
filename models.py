from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100,blank=True)
    password=models.CharField(max_length=100)
    create_at= models.DateField(auto_now_add=True)
    is_admin= models.BooleanField( default=False)
    is_staff= models.BooleanField( default=False)
    SearchableFields=['name','email','id']

    def __str__(self):
        return self.name








