from django.shortcuts import render
from .forms import FormDataForm

# Create your views here.
def render_form(request):
  form = FormDataForm()
  return render(request, 'form_template.html', {'form': form})