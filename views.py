import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    index_html = open("content/index.html").read()
    context = {
    "content": index_html,
    "title": "Home",
    }
    return render(request,"base.html", context)

def blog(request):
    blog_html = open("content/blog.html").read()
    context = {
    "content": blog_html,
    "title": "Blog",
    }
    return render(request, "base.html", context)


def purchase(request):
    purchase_html = open("content/purchase.html").read()
    context = {
    "content": purchase_html,
    "title": "Purchase"
    }
    return render(request, "base.html", context)


def send_email(request):
    context = {}
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]

    emailcontent.objects.create(
        name=name,
        email=email,
        message=message,
    )
    return render(request, 'send_email.html', context)
    # return redirect("/") # Return a redirect!


# def add_dog(request):
#     context = {}

#     # First, check if they have submitted something:
#     if 'dogname' in request.POST:

#         # Then, get the data out of the POST dictionary
#         name = request.POST['dogname']
#         age = request.POST['age']
#         time = request.POST['time']
#         date = request.POST['date']

#         # Finally, actually create the appointment
#         DogAppointment.objects.create(
#             name=name,
#             age=age,
#             date=date,
#             time=time,
#         )

#     return render(request, 'add_dog.html', context)