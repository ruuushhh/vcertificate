from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import cer
from .forms import Upload_form
from django.contrib.auth.decorators import login_required


# Create your views here.


class CerList(LoginRequiredMixin, ListView):
    model = cer
    context_object_name = 'documents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = context['documents'].filter(
            user=self.request.user)
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['documents'] = context['documents'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input
        return context


class CerDetail(LoginRequiredMixin, DetailView):
    model = cer
    context_object_name = 'document_detail'
    template_name = 'docs/cer.html'


@login_required()
def CerCreate(request):
    if request.method == 'POST':
        form = Upload_form(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            the_description = form.cleaned_data['file_description']
            the_activity = form.cleaned_data['file_activity']
            the_year = form.cleaned_data['file_year']

            cer(title=name, files=the_files, user=request.user, activity=the_activity, issue_year=the_year,
                description=the_description).save()
            return redirect('cer_list')
        else:
            return HttpResponse("error")
    else:
        context = {
            'form': Upload_form()
        }
        return render(request, 'cer_form.html', context)


class CerUpdate(LoginRequiredMixin, UpdateView):
    model = cer
    fields = ['title', 'description', 'issue_year']
    success_url = reverse_lazy('cer_list')


class CerDelete(LoginRequiredMixin, DeleteView):
    model = cer
    context_object_name = "document_detail"
    success_url = reverse_lazy('cer_list')
