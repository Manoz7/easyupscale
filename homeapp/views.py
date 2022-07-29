from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib import messages

from homeapp.models import Contact, MeetRequest


# Create your views here.


class Home(TemplateView):
    template_name = 'homeapp/index.html'


class Contact(CreateView):
    model = Contact
    fields = ["fullname", "email", "phone", "message"]
    template_name = 'homeapp/contact.html'

    def get_success_url(self):
        messages.success(self.request, 'Form Submitted Successfully!')
        return self.request.META['HTTP_REFERER']


# def contact(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         message = request.POST['message']
#
#         if fullname != "" and email != "" and phone != "" and message != "":
#             mycontact = Contact(fullname=fullname, email=email, phone=phone, message=message)
#             # print(ct.fullname)
#             mycontact.save()
#
#     return render(request, 'homeapp/contact.html')

# class Contact(View):
#     def get(self, request):
#         return render(request, 'homeapp/contact.html')
#
#     def post(self, request):
#         contact_dict = dict(
#             fullname=request.POST.get('fullname'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             message=request.POST.get('message'),
#
#         )
#         if not all(contact_dict.values()):
#             # raise error
#             pass
#
#         Contact.objects.create(
#             **contact_dict
#         )
#         return render(request, 'homeapp/contact.html')

class About(TemplateView):
    template_name = 'homeapp/about.html'


class Blog(TemplateView):
    template_name = 'homeapp/blog-grids.html'


class BlogDetail(TemplateView):
    template_name = 'homeapp/blog-details.html'


class HandleLogin(TemplateView):
    template_name = 'homeapp/signin.html'


class MeetingRequest(CreateView):
    model = MeetRequest
    template_name = 'homeapp/signup.html'
    fields = ["company_name", "country", "location", "zip_code", "email", "field_of_work", "phone_number", "rpr_name", "rpr_post" ]

    def get_success_url(self):
        messages.success(self.request, "Success! We'll get back to you right away.")
        return self.request.META['HTTP_REFERER']
