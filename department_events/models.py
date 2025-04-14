from django.db import models
from accounts.models import Profile, Podrazdelenie


class DepartmentEventType(models.Model):
    name = models.CharField("Название", max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тип события подразделения"
        verbose_name_plural = "Типы событий подразделений"

    def __str__(self):
        return self.name


class DepartmentEventName(models.Model):
    name = models.CharField("Название", max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Название события подразделения"
        verbose_name_plural = "Названия событий подразделений"

    def __str__(self):
        return self.name


class DepartmentEventLocation(models.Model):
    name = models.CharField("Место", max_length=255)
    department = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Место события подразделения"
        verbose_name_plural = "Места событий подразделений"

    def __str__(self):
        return self.name


class DepartmentEvent(models.Model):
    datetime = models.DateTimeField("Дата и время")
    department = models.ForeignKey(Podrazdelenie, verbose_name="Подразделение", on_delete=models.CASCADE)
    type = models.ForeignKey(DepartmentEventType, verbose_name="Тип", on_delete=models.CASCADE)
    name = models.ForeignKey(DepartmentEventName, verbose_name="Название", on_delete=models.CASCADE)
    location = models.ForeignKey(DepartmentEventLocation, verbose_name="Место", on_delete=models.CASCADE)
    description = models.TextField("Описание", blank=True)
    staff = models.ManyToManyField(Profile, verbose_name="Сотрудники", blank=True)

    class Meta:
        verbose_name = "Событие подразделения"
        verbose_name_plural = "События подразделений"

    def __str__(self):
        return f"{self.name} ({self.type}) @ {self.datetime.strftime('%Y-%m-%d %H:%M')}"
