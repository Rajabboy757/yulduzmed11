from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from newclients.forms import Messages
from newclients.models import News, Doctor, Review, Message
from django.template import loader


# pages begin
def home(request):
    context = {}

    news_context = {"news": News.objects.all()}
    doctors_context = {"doctors": Doctor.objects.all()}
    reviews_context = {"reviews": Review.objects.all()}
    content = loader.render_to_string("base.html", context, request)
    content += loader.render_to_string("includes/hero.html", context, request)
    content += loader.render_to_string("includes/news.html", news_context, request)
    content += loader.render_to_string("includes/service.html", context, request)
    content += loader.render_to_string("includes/team.html", doctors_context, request)
    content += loader.render_to_string("includes/about.html", context, request)
    content += loader.render_to_string("includes/testimonial.html", reviews_context, request)
    content += loader.render_to_string("includes/appointment.html", context, request)
    content += loader.render_to_string("includes/contact.html", context, request)
    content += loader.render_to_string("includes/footer.html", context, request)

    form = Messages(request.GET)
    if form.is_valid():
        form_data = form.cleaned_data
        obj = Message()

        obj.first_name = form_data.get("first_name")
        obj.phone = form_data.get("phone")
        obj.doctor = form_data.get("doctor")
        obj.date = form_data.get("date")
        obj.time = form_data.get("time")

        obj.save()
        return redirect('/')
    else:
        # return HttpResponse("Oops something went wrong")

        return HttpResponse(content, None, None)


# def new_client_view(request):
#     form = Messages(request.GET)
#     if form.is_valid():
#         form_data = form.cleaned_data
#         obj = Message()
#
#         obj.first_name = form_data.get("first_name")
#         obj.phone = form_data.get("phone")
#         obj.doctor = form_data.get("doctor")
#         obj.date = form_data.get("date")
#         obj.time = form_data.get("time")
#
#         obj.save()
#         return redirect('/')
#     return HttpResponse("Oops something went wrong")

    # else:
    #     form = Messages()
    #
    # return render(request, 'includes/appointment.html', {'form': form})

# def about(request):
#     return render(request, 'includes/about.html')
#
#
def home1(request):
    return render(request, 'includes/hero.html')
#
#
# def appointment(request):
#     return render(request, 'includes/appointment.html')
#
#
# def contact(request):
#     return render(request, 'includes/contact.html')
#
#
# def news_list_view(request):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}
#
#     # add the dictionary during initialization
#     context["dataset"] = News.objects.all()
#
#     return render(request, "includes/news.html", context)
#
# def service(request):
#     return render(request, 'includes/service.html')
#
#
# def team(request):
#     return render(request, 'includes/team.html')
#
#
# def testimonial(request):
#     return render(request, 'includes/testimonial.html')


# pages end

# def new_client_view(request, *args, **kwargs):
#     form = NewClientForm(request.POST)
#     if form.is_valid():
#         new_client = form.save()
#         new_client.save()
#         return redirect('/')
#
#     return HttpResponse("Oops something went wrong")
