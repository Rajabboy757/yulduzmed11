from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from newclients.forms import NewClientForm
from newclients.models import News


# pages begin
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'includes/about.html')


def appointment(request):
    return render(request, 'includes/appointment.html')


def contact(request):
    return render(request, 'includes/contact.html')


class NewsListView(ListView):
    model = News
    template_name = 'includes/news.html'


def service(request):
    return render(request, 'includes/service.html')


def team(request):
    return render(request, 'includes/team.html')


def testimonial(request):
    return render(request, 'includes/testimonial.html')


# pages end

def new_client_view(request, *args, **kwargs):
    form = NewClientForm(request.POST)
    if form.is_valid():
        new_client = form.save()
        new_client.save()
        return redirect('/')

    return HttpResponse("Oops something went wrong")
