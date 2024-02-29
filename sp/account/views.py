# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import FormView

from .forms import SpForm
from extensions import utils


class SP(LoginRequiredMixin, FormView):
    template_name = 'sp.html'
    form_class = SpForm

    def form_valid(self, form):
        template_text = form.cleaned_data['formsDotPyTextField']
        modified_text = utils.substring_adder(template_text)
        return self.render_to_response(self.get_context_data(form=form, textShownInHtml=modified_text))
