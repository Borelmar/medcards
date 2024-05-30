from django.db import models
from django.utils import timezone

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)
    note = models.TextField()

    def __str__(self):
        return f'Visit on {self.visit_date} for {self.client}'
