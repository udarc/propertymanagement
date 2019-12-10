from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import RentalProperty, RentalCategory, Image


class RestrictToOwnerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToOwnerMixin, self).get_queryset()
        qs = qs.filter(owner=self.request.user.userprofile)
        return qs

class RentalCategoryListView(ListView):
    model = RentalCategory
    queryset = RentalCategory.objects.all()
    template_name = "housing/category/rentalcategory_list.html"



class RentalCategoryCreateView(RestrictToOwnerMixin, CreateView):
    model = RentalCategory
    fields = ['title', "summary"]
    template_name = "housing/category/rentalcategory_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user.userprofile
        return super().form_valid(form)
    

class RentalCategoryDetailView(DetailView):
    queryset = RentalCategory.objects.all()
    template_name = "housing/category/rentalcategory_detail.html"
    

class RentalCategoryUpdateView(RestrictToOwnerMixin,UpdateView):
    model = RentalCategory
    fields = ['title', "summary"]
    template_name = "housing/category/rentalcategory_form.html"

class RentalCategoryDeleteView(RestrictToOwnerMixin, DeleteView):
    model = RentalCategory
    success_url = reverse_lazy('category-list')
    template_name = 'object_confirm_delete.html'