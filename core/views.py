from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bombeiro

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['bombeiro'] = Bombeiro.objects.all()
        return context
