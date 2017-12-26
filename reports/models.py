from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=100)
    report_date = models.DateField(auto_now_add=True)
    report_type = models.CharField(max_length=100, null=True)
    file_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name