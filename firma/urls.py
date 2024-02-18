from django.urls import path
from .views import *

urlpatterns=[
    path('api/tutorials',Mahsulot_view.as_view()),
    path('api/ish',Ishturi.as_view()),
    path('api/xato',Xato_view.as_view()),
    path('api/xato/missed',Missed_view.as_view()),
    path('api/xato/<int:id>',Detail.as_view())
    
]