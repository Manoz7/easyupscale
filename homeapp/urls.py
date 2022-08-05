from django.contrib import admin
from django.urls import path
from homeapp import views
from homeapp.views import Home, Contact, MeetingRequest, About, Blog, BlogDetail, HandleLogin, Pricing, BlogDetail2, BlogDetail3

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('contact', views.contact, name='contact'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('blog', Blog.as_view(), name='blog'),
    path('blogdetails/1', BlogDetail.as_view(), name='blogdetails'),
    path('signin', HandleLogin.as_view(), name='signin'),
    path('meet', MeetingRequest.as_view(), name='meet'),
    path('pricing', Pricing.as_view(), name='pricing'),
    
    
    # Blog details until dynamic
    path('blogdetails/2', BlogDetail2.as_view(), name='blogdetails2'),
    path('blogdetails/3', BlogDetail3.as_view(), name='blogdetails3'),
    
]
