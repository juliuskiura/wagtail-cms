from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


from careers.models import JobPostDetail

class JobApplication(models.Model):
    jobpost = models.ForeignKey(JobPostDetail, on_delete=models.SET_NULL, null=True, blank=True)
    jobtitle = models.CharField(max_length=250, null=True, blank=True)
    application_date =models.DateTimeField(default=timezone.now, null=True, blank=True)
    full_name= models.CharField(blank=False, null=False, max_length=100)
    email = models.EmailField(max_length=50) 
    phone_number = models.CharField(max_length=13)
    about_yourself = models.TextField()
    when_can_you_start = models.TextField()
    monthly_salary_expectations = models.DecimalField(
        decimal_places=2, max_digits=10)
    preferred_contract = models.CharField(blank=False, null=False, max_length=100)
    consent = models.BooleanField()

    document = models.FileField(upload_to='careers/')

    def __str__(self):
        return self.full_name


