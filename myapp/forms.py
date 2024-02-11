from django import forms
from django.conf import settings
from captcha.fields import CaptchaField
from django.core.mail import EmailMessage
from django.core.validators import FileExtensionValidator
from .models import Application

class ApplicationForm(forms.ModelForm):
    captcha = CaptchaField()
    age = forms.IntegerField(min_value=18, max_value=35)
    resume = forms.FileField(
    validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])],
    error_messages={'invalid_extension': 'Файл должен иметь формат DOC, DOCX или PDF'} 
)

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
        'position' : forms.Select(attrs={'empty_label': 'Frontend разработчик'}),
        'commercial_experience': forms.RadioSelect(),
        'certificates': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['age'].widget.attrs['placeholder'] = 'Мы рассматриваем кандидатов от 18 до 35'
        self.fields['education'].widget.attrs['placeholder'] = 'Колледж, вуз, курсы'
        self.fields['education'].widget.attrs['rows'] = 3
        self.fields['email'].widget.attrs['placeholder'] = 'Введите корректный email для связи'
        self.fields['work_experience'].widget.attrs['placeholder'] = 'За последние 5 лет'
        self.fields['work_experience'].widget.attrs['rows'] = 3
        self.fields['projects'].widget.attrs['placeholder'] = 'Ссылки на ваши проекты'
        self.fields['projects'].widget.attrs['rows'] = 3
        self.fields['resume'].widget.attrs['accept'] = '.pdf,.doc,.docx'     
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'}) 


 
    def get_message(self):
        subject = f'Добавлена анкета {self.instance.name}' 
        msg = str(self.instance)
        return subject, msg

    def send(self):
        subject, msg = self.get_message()

        email = EmailMessage(
        subject=subject,
        body=msg,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.RECIPIENT_ADDRESS],
        )
        email.attach_file(self.instance.resume.path)

        email.send()

