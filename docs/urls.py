from django.urls import path, register_converter
from docs.views import CerList, CerDetail, CerUpdate, CerDelete, CerCreate
from .utils import HashIdConverter

register_converter(HashIdConverter, "hashid")


urlpatterns = [
    path('cer_list/', CerList.as_view(), name='cer_list'),
    path('cer/<hashid:pk>/', CerDetail.as_view(), name='cer_detail'),
    path('cer_create/', CerCreate, name='cer_create'),
    path('cer_update/<hashid:pk>/', CerUpdate.as_view(), name='cer_update'),
    path('cer_delete/<hashid:pk>/', CerDelete.as_view(), name='cer_delete'),

]
