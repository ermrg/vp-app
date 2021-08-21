from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from app.services.analysis.demographyService import get_all_population, get_all_male_genders, get_all_female_genders, \
    get_all_other_genders


@login_required
def index(request):
    new_dict = dict()
    new_dict['total_population'] = get_all_population
    new_dict['male_genders'] = get_all_male_genders
    new_dict['female_genders'] = get_all_female_genders
    new_dict['other_genders'] = get_all_other_genders
    return render(request, 'app/backend/dashboard1.html', new_dict)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def page_not_found(request):
    return render(request, 'app/backend/layouts/404.html')
