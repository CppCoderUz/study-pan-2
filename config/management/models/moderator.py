from django.db import models
from django.contrib.auth.models import AbstractUser



class MainUser(AbstractUser):
    ''' Asosiy foydalanuvchilar uchun model '''
    father_name = models.CharField(max_length=100,null=True, blank=True, verbose_name='Otasining ismi')
    def __str__(self) -> str:
        if self.last_name and self.first_name:
            return '%s %s'%(self.last_name, self.first_name)
        else:
            return self.username
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = '1. Foydalanuvchi'




