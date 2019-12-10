from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Address


class RestrictToOwnerMixin(LoginRequiredMixin):

    def get_queryset(self):
        qs = super(RestrictToOwnerMixin, self).get_queryset()
        qs = qs.filter(owner=self.request.user.userprofile)
        return qs


class AddressListView(ListView):
    model = Address
    queryset = Address.objects.all()
    paginate_by = 4
    context_object_name = 'addresses'


class AddressDetailView(DetailView):
    queryset = Address.objects.all()


class AddressCreateView(CreateView):
    model = Address
    fields = ['street_address1', "street_address2", "city","state","zipcode" ,"country" ]
    # context_object_name = 'address'

    def form_valid(self, form):
        form.instance.owner = self.request.user.userprofile
        return super().form_valid(form)
    

class AddressUpdateView(RestrictToOwnerMixin, UpdateView):
    model = Address
    fields = ['street_address1', "street_address2", "city","state","zipcode" ,"country" ]

class AddressDeleteView(RestrictToOwnerMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('address-list')
    template_name = 'object_confirm_delete.html'


        