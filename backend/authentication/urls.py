from django.urls import path, include
from .views import TestView

urlpatterns = [

    path('test', TestView.as_view(), name="test"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]