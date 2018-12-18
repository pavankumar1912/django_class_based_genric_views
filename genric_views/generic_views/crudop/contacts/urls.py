from django.urls import path
from .views import ContactCreate,ContactDelete,ContactDetail,ContactList,ContactUpdate

urlpatterns = [
    path('',ContactList.as_view(),name = 'contact_list'),
    path('details/<int:pk>',ContactDetail.as_view(),name = 'contact_detail'),
    path('create/',ContactCreate.as_view(),name = 'contact_create'),
    path('delete/<int:pk>',ContactDelete.as_view(),name = 'contact_delete'),
    path('update/<int:pk>',ContactUpdate.as_view(),name = 'contact_edit'),

]