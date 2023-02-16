from django.urls import include
from . import views

urlpatterns=[
  path('',views.index)
]