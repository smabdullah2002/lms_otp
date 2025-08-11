from django.db import models
class Status(models.TextChoices):
    INITIALIZE= "Initialize",
    APPROVED= "Approved",
    EXPIRED= "Expired",