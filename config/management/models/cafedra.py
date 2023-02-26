
from management.models import MainUser
from django.db import models


class Cafedra(models.Model):
    ''' Kafedra '''
    name = models.CharField(max_length=200, verbose_name='Kafedra nomi', unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = '5. Kafedralar'


class CafedraEmployeePosition(models.Model):
    ''' Kafedra lavozimlari '''
    name = models.CharField(max_length=150, unique=True, verbose_name='Lavozim nomi')
    short_name = models.CharField(max_length=100, unique=True,null=True, blank=True, verbose_name='Lavozimning qisqa nomi')

    def __str__(self) -> str:
        return '%s (%s)'%(self.name, self.short_name)
    
    class Meta:
        verbose_name = 'Kafedra lavozimi'
        verbose_name_plural = 'Kafedra lavozimlari (<=>)'


class CafedraMember(models.Model):
    ''' Kafedra ishchilari '''
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    position = models.ForeignKey(CafedraEmployeePosition, on_delete=models.CASCADE, verbose_name='Lavozimi')
    cafedra = models.ForeignKey(Cafedra, on_delete=models.CASCADE, verbose_name='Kafedra nomi')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqami')
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return '%s %s (%s)'%(str(self.user), self.position.name, self.cafedra.name)
    
    class Meta:
        verbose_name = 'Kafedra hodimi'
        verbose_name_plural = '6. Kafedra hodimlari'