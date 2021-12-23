def finish_save(form, request):    
    instance = form.save()
    visitor = instance.full_name
   
    data = {
        'form_saved': True,       
        'success': f'Hi, {visitor}. Thank you for your message. We will get back to you soon'
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
