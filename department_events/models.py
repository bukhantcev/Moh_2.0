from django.db import models
from accounts.models import Profile, Podrazdelenie


class DepartmentEventType(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DepartmentEventName(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DepartmentEventLocation(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DepartmentEvent(models.Model):
    datetime = models.DateTimeField()
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)
    type = models.ForeignKey(DepartmentEventType, on_delete=models.CASCADE)
    name = models.ForeignKey(DepartmentEventName, on_delete=models.CASCADE)
    location = models.ForeignKey(DepartmentEventLocation, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    staff = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return f"{self.name} ({self.type}) @ {self.datetime.strftime('%Y-%m-%d %H:%M')}"
