from typing import Iterable
from django.db import models


class Tovar(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi")
    slug = models.CharField(max_length=50)
    # one-to-many (Kategoriya <- Tovar'lar)
    # kategoriya_id
    kategoriya = models.ForeignKey("core.Kategoriya", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    discount = models.IntegerField(verbose_name="Chegirma", default=0)

    def __str__(self):
        return f"[{self.id}] - {self.name}"
    
    class Meta:
        verbose_name_plural = "Tovarlar"
        permissions = [
            ("with_discount", "Can set discount")
        ]


# bu pivot table - many-to-many
class TovarlarTeglar(models.Model):
    # one-to-many (Tovar <- TovarlarTeglar)
    tovar = models.ForeignKey("core.Tovar", on_delete=models.CASCADE)
    # one-to-many (Teg <- TovarlarTeglar)
    teg = models.ForeignKey("core.Teg", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.id}] - Tovar: {self.tovar.name}, Teg: {self.teg.name}"
    
    class Meta:
        verbose_name = "Tovarlar va Teglar"
        verbose_name_plural = "Tovarlar va Teglar"


class Kategoriya(models.Model):
    name = models.CharField(max_length=50)
    ota_kategoriya = models.ForeignKey("core.Kategoriya", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"[{self.id}] - {self.name}"
    
    class Meta:
        verbose_name_plural = "Kategoriyalar"



# bu pivot table - many-to-many
class KategoriyalarTeglar(models.Model):
    # one-to-many (Kategoriya <- KategoriyalarTeglar)
    kategoriya = models.ForeignKey("core.Kategoriya", on_delete=models.CASCADE)
    # one-to-many (Teg <- KategoriyalarTeglar)
    teg = models.ForeignKey("core.Teg", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.id}] - Kategoriya: {self.kategoriya.name}, Teg: {self.teg.name}"

    class Meta:
        verbose_name = "Kategoriyalar va Teglar"
        verbose_name_plural = "Kategoriyalar va Teglar"



class Teg(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.id}] - {self.name}"
    
    class Meta:
        verbose_name_plural = "Teglar"


class User(models.Model):
    pass

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# 901234567
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=9)
    REQUIRED_FIELDS = ["email", "phone_number"]