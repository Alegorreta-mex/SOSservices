from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required


class AuthBaseTemplateView(LoginRequiredMixin, TemplateView):
    title = ""

    def get_context_data(self, **kwargs):
        context = {
            "title": self.title,
            **kwargs,
        }
        return context


class AuthBaseCreateView(LoginRequiredMixin, CreateView):
    title = ""

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": self.title,
            **kwargs
        })
        return ctx


class AuthBaseListView(LoginRequiredMixin, ListView):
    title = ""

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": self.title,
            **kwargs
        })
        return ctx


class AuthBaseUpdateView(LoginRequiredMixin, UpdateView):
    title = ""

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": self.title,
            "pk": self.kwargs.get("pk", -1),
            **kwargs
        })
        return ctx


class AuthBaseDeleteView(LoginRequiredMixin, DeleteView):
    title = ""

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": self.title,
            **kwargs
        })
        return ctx


class BlankIndexView(AuthBaseTemplateView):
    template_name = "general/BlankIndexPage.html"
    title = "Blank Index"


class BlankPageView(AuthBaseTemplateView):
    template_name = "general/BlankIndexPage.html"
    title = "Blank page"
