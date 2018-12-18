from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse_lazy

# Create your views here.

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact
    #fields = '__all__'
class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'
class ContactUpdate(UpdateView):
    model = Contact
    fields = '__all__'

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')





