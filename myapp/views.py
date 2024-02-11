from django.contrib import messages
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ApplicationForm
from django.urls import reverse_lazy
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

class SuccessView(TemplateView):
    template_name = 'success.html'

class ApplicationView(FormView):
    form_class = ApplicationForm
    template_name = 'application.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        application = form.save()
        form.send()
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)



def refresh_captcha(request):
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        raise Http404

    new_key = CaptchaStore.pick()
    to_json_response = {
        "key": new_key,
        "image_url": captcha_image_url(new_key),
    }
    return JsonResponse(to_json_response)
