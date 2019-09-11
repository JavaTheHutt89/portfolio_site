from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView


def index(request):
    return render(request, 'core/core.html')


class CoreTemplateView(TemplateView):
    template_name = 'core/core.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = Info.objects.first()
        context['info'] = info
        context['workExperience'] = info.workexperience_set.order_by('-position_time')
        context['skills'] = info.skill_set.all()
        context['education'] = info.education_set.all()
        context['language'] = info.language_set.all()
        context['interests'] = info.interest_set.all()

        return context
