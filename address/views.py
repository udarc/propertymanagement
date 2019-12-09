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


# class ClientDetailView(RestrictToOwnerMixin, DetailView):
#     model = Client
#     slug_field = 'uuid'


# class ClientCreateView(LoginRequiredMixin, CreateView):
#     model = Client
#     fields = ['name', 'description', 'address_one', 'address_two', 'city',
#               'state', 'zip_code', 'country', 'phone']

#     def get_context_data(self, **kwargs):
#         context = super(ClientCreateView, self).get_context_data(**kwargs)
#         context.update({'input': 'Create Client', 'title': 'Add a New Client'})
#         return context

#     def form_valid(self, form):
#         client = form.save(commit=False)
#         client.owner = self.request.user
#         return super(ClientCreateView, self).form_valid(form)

#     def get_success_url(self):
#         return reverse('clients:client_list')


# class ClientUpdateView(RestrictToOwnerMixin, UpdateView):
#     model = Client
#     fields = ['name', 'description', 'address_one', 'address_two', 'city',
#               'state', 'zip_code', 'country', 'phone']
#     slug_field = 'uuid'

#     def get_context_data(self, **kwargs):
#         context = super(ClientUpdateView, self).get_context_data(**kwargs)
#         context.update({'input': 'Update Client', 'title': 'Update Client'})
#         return context

#     def get_success_url(self):
#         return reverse('clients:client_detail', kwargs={'slug': self.object.uuid})


# class ClientDeleteView(RestrictToOwnerMixin, DeleteView):
#     model = Client
#     slug_field = 'uuid'
#     template_name = 'object_confirm_delete.html'

#     def get_success_url(self):
#         return reverse('clients:client_list')
        