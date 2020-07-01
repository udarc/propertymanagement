from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import FormView , TemplateView
from django.utils.timezone import now
from .forms import ContactForm
from django.shortcuts import render




#https://wsvincent.com/django-contact-form/
# https://data-flair.training/blogs/django-send-email/
class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('success')
    template_name = 'contact.html'


    def form_valid(self, form):
        from_email=form.cleaned_data.get('sender_email').strip()
        subject=f'Message from {form.cleaned_data.get("name").strip()}'
        topic = name=form.cleaned_data.get('subject').strip()
        message = form.cleaned_data.get('message').strip()
        message = "Topic: {0} \nEmail: {1} Message: \n\n{2}".format(topic,from_email,message)
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email= from_email,
                recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],  
            )
        except BadHeaderError:
            return HttpResponse("Invalid header")
        return super(ContactView, self).form_valid(form)




# https://hellowebbooks.com/news/introduction-to-class-based-views/

class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        if now().weekday() < 5 and 8 < now().hour < 18:
            context['open'] = True
        else:
            context['open'] = False
        return context

class HomeView(TemplateView):

    template_name = 'index.html'
    #  def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context['latest_rentals'] =  RentalProperty.objects.all().order_by('-id')[:3]
    #     return context


def custom_404(request,exception=None ):
    return render(request, '404.html', status=404)

def custom_500(request,exception=None):
    return render(request, '500.html', status=500)