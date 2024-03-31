from django.shortcuts import render, redirect
from .forms import FormDataForm

# Create your views here.
def render_form(request):
  form = FormDataForm()
  return render(request, 'form_template.html', {'form': form})

def submit_form(request):
  if request.method == 'POST':
    form = FormDataForm(request.POST)
    return redirect('success_page')
  else:
    form = FormDataForm()
    return render(request, 'form_template.html', {'form': form})