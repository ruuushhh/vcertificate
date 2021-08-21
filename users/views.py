from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, Profile_form
from django.contrib.auth.decorators import login_required
from users.models import profile
from django.contrib.auth.mixins import LoginRequiredMixin
from docs.models import cer
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form1 = UserRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form1 = UserRegisterForm()

    return render(request, 'register.html', {'form': form1})


@login_required()
def Profile_edit(request, *args, **kwargs):
    if request.method == 'POST':
        form = Profile_form(request.POST)

        if form.is_valid():
            the_f_name = form.cleaned_data['form_f_name']
            the_l_name = form.cleaned_data['form_l_name']
            the_email = form.cleaned_data['form_email']
            the_phone = form.cleaned_data['form_phone']
            the_year = form.cleaned_data['form_year']
            the_skills = form.cleaned_data['form_skills']

            profile(f_name=the_f_name, l_name=the_l_name, email=the_email,
                    user=request.user, phone=the_phone, year=the_year, skills=the_skills).save()

            return redirect('profile')
        else:
            return HttpResponse("error")
    else:
        context = {
            'form': Profile_form()
        }
    return render(request, 'profile_form.html', context)


@login_required()
def profile_view(request):
    try:
        obj = profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        return redirect('profile_edit')
    context = {
        'f_name': obj.f_name,
        'l_name': obj.l_name,
        'id': obj.id,
        'email': obj.email,
        'phone': obj.phone,
        'year': obj.year,
        'skills': obj.skills

    }
    return render(request, 'profile.html', context)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = profile
    fields = ['f_name', 'l_name', 'email', 'phone', 'skills', 'year']
    success_url = reverse_lazy('profile')
