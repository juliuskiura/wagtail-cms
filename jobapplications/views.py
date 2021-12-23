from django.http import JsonResponse
from careers.models import JobPostDetail
from django.shortcuts import render, redirect
from django.contrib import messages
from. forms import JobApplicationForm
from .response_setter import finish_save, invalidform
# Create your views here.


def job_application(request, slug):   
    jobpost = JobPostDetail.objects.get(slug=slug)
    
    form = JobApplicationForm()
   
    form.fields['jobpost'] = jobpost
    if request.method == 'POST':

        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            data = finish_save(form, request)
            data["updated"] = True
            return JsonResponse(data)
        else:
            data = invalidform(form)
            return JsonResponse(data)
           
    context = {
        'form': form,
     
        'jobpost': jobpost,
        'add_careers_css': 'add_careers_css',

    }
    return render(request, 'jobapplications/form_page.html', context)
