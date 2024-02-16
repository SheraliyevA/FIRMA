from django.urls import path
from .views import *

urlpatterns=[
    path('api/tutorials',Mahsulot_view.as_view()),
    path('api/ish',Ishturi.as_view()),
]