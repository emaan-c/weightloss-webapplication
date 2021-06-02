from django.shortcuts import render, redirect
from .models import Info, Calorie
from .forms import InfoForm, CalorieForm

def get_cal(request):
    Info.objects.all().delete()
    Calorie.objects.all().delete()
    context = {}
    if request.method == 'POST':
        form1 = CalorieForm(request.POST or None)
        form2 = InfoForm(request.POST or None)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('chart')
    else:
        form1 = CalorieForm()
        form2 = InfoForm()
    context['form1'] = form1
    context['form2'] = form2
    return render(request, 'calorie/home.html', context)

