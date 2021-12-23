from django import forms

from .models import JobApplication
from captcha.fields import ReCaptchaField

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['jobpost', 'jobtitle', 'full_name', 
                    'email', 'phone_number', 'about_yourself',
                  'when_can_you_start', 'monthly_salary_expectations',
                  'preferred_contract', 'consent', 'document',
            

                 ]
        exclude = ('application_date',)
        labels = {
            'name': 'Business Name'
        }


'''


jobpost = models.ForeignKey(JobPostDetail, on_delete=models.SET_NULL, null=True, blank=True)
    jobtitle = models.CharField(max_length=250, null=True, blank=True)
    application_date =models.DateTimeField(default=timezone.now, null=True, blank=True)
    full_name= models.CharField(blank=False, null=False, max_length=100)
    email = models.EmailField(max_length=50) 
    phone_number = PhoneNumberField()
    about_yourself = models.TextField()
    when_can_you_start = models.TextField()
    monthly_salary_expectations = models.DecimalField(
        decimal_places=2, max_digits=10)
    preferred_contract = models.CharField(blank=False, null=False, max_length=100)
    consent = models.BooleanField()

    document = models.FileField(upload_to='careers/')



'''