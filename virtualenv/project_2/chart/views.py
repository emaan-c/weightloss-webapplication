from django.shortcuts import render
from calorie.models import Calorie,Info
from django.views.generic import TemplateView

class ChartView(TemplateView):
    template_name = 'chart/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Calorie.objects.all()
        context["js"] = Info.objects.all()
        return context




# delete the querybase after a user inputs his calories
