from management.models import MainUser
from django.db import models



class PositionEmployeeFaculty(models.Model):
    ''' Fakultet lavozimlari '''
    name = models.CharField(max_length=150, verbose_name='Lavozim', unique=True)
    short_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Lavozim (qisqa nomi)')

    def __str__(self) -> str:
        if self.short_name:
            return '%s %s' %(self.name, self.short_name)
        else:
            return self.name
    
    class Meta:
        verbose_name = 'Fakultet lavozimi'
        verbose_name_plural = 'Fakultet lavozimlari (<=>)'


class Faculty(models.Model):
    ''' Fakultet '''
    name = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = '3. Fakultetlar'



class FacultyMember(models.Model):
    ''' Fakultetga oid hodimlar '''
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Fakultet nomi')
    position = models.ForeignKey(PositionEmployeeFaculty, on_delete=models.CASCADE, verbose_name='Darajasi')
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    phone_number = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self) -> str:
        return '%s %s (%s)'%(str(self.user), self.faculty.name, self.position.short_name)
    
    class Meta:
        verbose_name = 'Fakultet hodimi'
        verbose_name_plural = '4. Fakultet hodimlari'