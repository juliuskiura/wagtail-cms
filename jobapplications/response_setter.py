from careers.models import JobPostDetail
from django.shortcuts import get_object_or_404
def finish_save(form, request):    

    instance = form.save(commit=False)
    jobpost = get_object_or_404(JobPostDetail, slug=instance.jobtitle)
    instance.jobpost = jobpost
    instance.jobtitle = jobpost.title   
    saved_instance = form.save()
    applicant = saved_instance.full_name

   
    data = {
        'form_saved': True,       
        'success': f'Hi, {applicant}. Thank you, for your interest in our company. We do appreciate the time that you invested in this application. Please wait as we conduct our review. We will get back to you. '
    }
    return data


def invalidform(form):
    data = {}
    """
        This loops through the form.errors to take the errors that are returned by invalid form. The errors are in form of a dictionary hence we loop with key, value, and to recreate a new dictionary that would be easily used by ajax as a json
            """
    for field, errors in form.errors.items():

        field = field
        errors = ','.join(errors)
        new_error = {field: errors}

        data.update(new_error)

    return data
