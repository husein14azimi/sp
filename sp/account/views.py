# from django.http import HttpResponse
from django.shortcuts import render
from .forms import MainForm
from extensions import utils


def home(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            template_text = form.cleaned_data['formsDotPyTextField']
            modified_text = utils.substring_adder(template_text)
            return render(request, 'home.html', {'textShownInHtml': modified_text})
    else:
        form = MainForm()
    return render(request, 'home.html', {'form': form})
