from django.urls import path
from .views import RetrieveBasicInfo


urlpatterns = [
    path('', RetrieveBasicInfo.as_view(), name='info')
]
