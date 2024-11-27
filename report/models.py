from typing import Iterable
from django.db import models
from bot.models import TelegramUser

class Book(models.Model):
    user = models.ForeignKey(to=TelegramUser, on_delete=models.CASCADE, blank=True, null=True)
    date = models.IntegerField()
    title = models.CharField(max_length=200)
    page = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs) -> None:
        if self.user is not None and self.date and self.title and self.page:
            super().save(*args, **kwargs)