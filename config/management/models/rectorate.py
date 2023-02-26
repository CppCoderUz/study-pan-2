from management.models import MainUser
from django.db import models


class LeadershipPosition(models.Model):
    ''' Rahbariyatdagilarning lavozimlari '''
    name = models.CharField(max_length=150, verbose_name='Lavozim nomi')
    short_name = models.CharField(max_length=100, unique=True, verbose_name='Lavozimning qisqa nomi')

    def __str__(self) -> str:
        return '%s %s'%(self.name, self.short_name)
    
    class Meta:
        verbose_name = 'Dekanat lavozimi'
        verbose_name_plural = 'Dekanat lavozimlari (<=>)'




class Leadership(models.Model):
    ''' Rahbariyat modeli '''
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    position = models.ForeignKey(LeadershipPosition, on_delete=models.CASCADE, verbose_name='Lavozimi')
    
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefon raqami')

    def __str__(self) -> str:
        return '%s %s'%(str(self.user), self.position.short_name)

    class Meta:
        verbose_name = 'Rahbar'
        verbose_name_plural = '2. Rahbarlar'