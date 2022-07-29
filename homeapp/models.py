from django.db import models

# Create your models here.


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.fullname


# Request a Meeting
class MeetRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    company_name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=25, default='Nepal')
    location = models.CharField(max_length=50, null=False)
    zip_code = models.IntegerField()
    email = models.EmailField()                                 #Office mail
    field_of_work = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)                    #Office phone
    rpr_name = models.CharField(max_length=50)                  #Representative full name
    rpr_post = models.CharField(max_length=50)                  #Representative designation

    def __str__(self):
        return f' {self.rpr_name} and {self.company_name}'
