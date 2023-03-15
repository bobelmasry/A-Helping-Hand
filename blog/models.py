from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    short_job_description = models.TextField(max_length=300)
    content = models.TextField(max_length=3000)
    job_requirements = models.TextField(max_length=3000)


    Learning_disabilities = models.BooleanField()
    Hearing_loss = models.BooleanField()
    Cerebral_palsy = models.BooleanField()
    Physical_disability = models.BooleanField()
    Vision_impairment = models.BooleanField()
    Dyslexia = models.BooleanField()
    Stroke = models.BooleanField()
    Diabetes = models.BooleanField()
    Spinal_cord_injury = models.BooleanField()
    Parkinsons_disease = models.BooleanField()
    Neurological_disorder = models.BooleanField()


    contact_info = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
