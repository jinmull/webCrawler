from django.db import models

# Create your models here.
class Member(models,Model):
    assembly_id = models.IntegerField(null=True)
    kr_name = models.CharField(max_length=20)
    chi_name = models.CharField(max_length=20)
    en_name = models.CharField(max_length=20)

    def __str__(self):
        return self.kr_name