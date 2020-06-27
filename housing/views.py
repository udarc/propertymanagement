from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import RentalProperty, RentalCategory, Image
from .forms import RentalPropertyForm

from address.models import Address


class RestrictToOwnerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToOwnerMixin, self).get_queryset()
        qs = qs.filter(owner=self.request.user.userprofile)
        return qs


class RentalCategoryListView(ListView):
    model = RentalCategory
    queryset = RentalCategory.objects.all()
    template_name = "housing/category/rentalcategory_list.html"
    paginate_by = 4



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
    success_url = reverse_lazy('housing:category-list')
    template_name = 'object_confirm_delete.html'

#Rental properties

class GetObjectMixin(object):

    def get_object(self, queryset=None):
        obj = super(GetObjectMixin, self).get_object()
        if not obj.owner == self.request.user.userprofile:
            raise Http404
        category = RentalCategory.objects.get(slug=obj.category.slug)
        address = Address.objects.get(pk=obj.address.id)
        return obj



class RentalPropertyListView(GetObjectMixin,ListView):
    model = RentalProperty
    queryset = RentalProperty.objects.all()
    paginate_by = 4
    template_name = "housing/property/rentalproperty_list.html"


class RentalPropertyCreateView(RestrictToOwnerMixin, CreateView):
    model = RentalProperty
    form_class= RentalPropertyForm
    template_name = "housing/property/rentalproperty_form.html"
    

    def form_valid(self, form):
        form.instance.owner = self.request.user.userprofile
        for photo in self.request.FILES.getlist('photos'):
            form.instance.photos = photo
            form.instance.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('housing:property-list')
"""    
class RentalCategoryPropertyCreateView(RestrictToOwnerMixin, CreateView):
    model = RentalProperty
    fields = ['name', 'rooms', 'size', 'amenities', 'price']
    template_name = "housing/property/rentalproperty_form.html"
    

    # def get_context_data(self, **kwargs):
    #     context = super(RentalPropertyCreateView, self).get_context_data(**kwargs)
    #     # context.update({'input': 'Create Contact',
    #     #                 'title': 'Add a New Contact'})
    #     return context

    def form_valid(self, form):
        new_rentalproperty = form.save(commit=False)
        new_rentalproperty.owner = self.request.user.userprofile
        rentalcategory = RentalCategory.objects.get(pk=self.kwargs['id'])
        address = Address.objects.get(pk=self.kwargs['location_id'])
        new_rentalproperty.propertyType = rentalcategory
        new_rentalproperty.location = address
        new_rentalproperty.save()
        return super(RentalPropertyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('housing:category-list')
    
"""
class RentalPropertyDetailView(DetailView):
    queryset = RentalProperty.objects.all()
    template_name = "housing/property/rentalproperty_detail.html"
    

class RentalPropertyUpdateView(RestrictToOwnerMixin,UpdateView):
    model = RentalProperty
    # fields = ['name', 'location','propertyType','rooms', 'size','photos' ,'amenities', 'price']
    form_class= RentalPropertyForm
    template_name = "housing/property/rentalproperty_form.html"

class RentalPropertyDeleteView(RestrictToOwnerMixin, DeleteView):
    model = RentalProperty
    success_url = reverse_lazy('housing:property-list')
    template_name = 'object_confirm_delete.html'