from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'loggedin.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("loggedin"))
        return super().get(request, *args, **kwargs)


class AdminPage(TemplateView):
    template_name = "adminindex.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("adminlogin"))
        return super().get(request, *args, **kwargs)

