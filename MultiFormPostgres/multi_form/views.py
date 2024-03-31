from django.shortcuts import render
from .models import FormData

# Create your views here.
# def render_form(request):
#     if request.method=='POST':
#       name=request.POST['name']
#       phone=request.POST['phone']
#       email=request.POST['email']
#       address=request.POST['address']
#       data = FormData(name=name, phone=phone, email=email, address=address)
#       data.save()
#       # print(name, phone, email, address)
#     return render(request, 'form_template.html')

def render_form(request):
    if request.method == 'POST':
        form_data_list = []
        for key in request.POST.keys():
            if key.startswith('name'):
                index = key.split('_')[-1]
                name = request.POST.get(f'name_{index}')
                email = request.POST.get(f'email_{index}')
                phone = request.POST.get(f'phone_{index}')
                address = request.POST.get(f'address_{index}')
                if name and email and phone and address:
                    form_data = FormData(name=name, email=email, phone=phone, address=address)
                    form_data_list.append(form_data)
        
        # Save all form data instances in one go
        FormData.objects.bulk_create(form_data_list)

    return render(request, 'form_template.html')