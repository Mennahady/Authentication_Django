from django.db import models
from django.conf import settings

class Diagnosis(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='skin_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'diagnoses'

    def __str__(self):
        return f"Diagnosis for {self.patient.email} on {self.created_at}"

class Prediction(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, related_name='predictions', on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    probability = models.FloatField()  # Store as decimal between 0 and 1
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-probability']

    def __str__(self):
        return f"{self.condition}: {self.probability * 100}%"
