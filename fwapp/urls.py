from django.urls import path 
from .views import Myview

urlpatterns=[
    path('',Myview.as_view()),
    path('my/<int:id>/',Myview.as_view())
]