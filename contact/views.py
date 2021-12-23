from django.shortcuts import render
import json
from .response_setter import finish_save, invalidform
from django.http import JsonResponse
from. forms import ModelContactForm

# Create your views here.


def contact_form_view(request):  
    form = ModelContactForm() 
    if request.method == 'POST':
        form = ModelContactForm(request.POST, request.FILES)
        if form.is_valid():
            data = finish_save(form, request)    
            data["updated"]= True
            return JsonResponse(data)
        else:
            data = invalidform(form)
            return JsonResponse(data)
    context = {
        'form': form,

    }
    return render(request, 'contact/ajaxed_form_page.html', context)
