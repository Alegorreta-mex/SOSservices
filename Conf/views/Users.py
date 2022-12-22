from django.urls import reverse_lazy
from django.views.generic import CreateView

from Conf.forms.Users import SignUpForm
from Main.DefaultViews.GeneralViews import AuthBaseCreateView, AuthBaseTemplateView


class SignUpViewAuth(CreateView):
    title = "Registration"
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


