from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['id']
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return f"{self.name}"

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    POSITIONS = [
        ('frontend', 'Frontend разработчик'),
        ('backend', 'Backend разработчик'),
        ('mobile', 'Mobile разработчик'),
        ('devops', 'DevOps инженер'),
        ('qa', 'Тестировщик'),
    ]
    position = models.CharField(max_length=100, choices=POSITIONS, default='frontend')   
    COMMERCIAL_EXPERIENCE_CHOICES = [
        (True, 'Есть'),
        (False, 'Нет')
    ]
    commercial_experience = models.BooleanField(choices=COMMERCIAL_EXPERIENCE_CHOICES, default=True)
    education = models.TextField()
    certificates = models.ManyToManyField(Certificate, blank=True)
    work_experience = models.TextField()
    projects = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    

    class Meta:
        ordering = ['id']
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        POSITIONS_DICT = dict(self.POSITIONS)
        return f"{self.name} с образованием {self.education} прислал резюме на вакансию {POSITIONS_DICT.get(self.position)}"

