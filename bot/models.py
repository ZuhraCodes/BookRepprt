from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True, default='default_value')
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name
    

