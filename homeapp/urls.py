from django.contrib import admin
from django.urls import path
from homeapp import views
from homeapp.views import Home, Contact, MeetingRequest, About, Blog, BlogDetail, HandleLogin

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('contact', views.contact, name='contact'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('blog', Blog.as_view(), name='blog'),
    path('blogdetails', BlogDetail.as_view(), name='blogdetails'),
    path('signin', HandleLogin.as_view(), name= 'signin'),
    path('meet', MeetingRequest.as_view(), name='meet'),

]
