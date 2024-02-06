# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import MainForm
from extensions import utils


def sp(request):
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            template_text = form.cleaned_data['formsDotPyTextField']
            modified_text = utils.substring_adder(template_text)
            return render(request, 'sp.html', {'textShownInHtml': modified_text})
    else:
        form = MainForm()
    return render(request, 'sp.html', {'form': form})


def logoutpage(request):
    return render(request, 'registration/logoutconfirmation.html')
