from django.urls import path
from .views import *


urlpatterns = [
    path('', Index, name='index'),
    path('a404/', A404, name='a404'),
    path('about/', About, name='about'),
    path('contact/', Contact_Data, name='contact'),
    path('property_agent/', Property_Agent, name='property_agent'),
    path('property_list/', Property_List, name='property_list'),
    path('property_type/', Property_Type, name='property_type'),
    path('testimonial/', Testimonial, name='testimonial'),
    path('home/<int:pk>/', post_detail, name='home_detail')
]