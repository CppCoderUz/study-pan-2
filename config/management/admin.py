from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.utils.translation import gettext_lazy as _



from management.models import (
    MainUser,
    LeadershipPosition,
    Leadership,
    PositionEmployeeFaculty,
    Faculty,
    FacultyMember,
    CafedraMember,
    Cafedra,
    CafedraEmployeePosition,
)

from study_plan.models import (
    Direction,
    Science,
    SemestrStudyPlan,
    ScienceStudyPlan,
    ProfessionalPractice,
)




class MainUserAdmin(UserAdmin):
    ''' Asosiy foydalanuvchilar '''
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('father_name',)}),
    ) 
admin.site.register(MainUser, MainUserAdmin)



# ==================================================================
# Dekanat sozlamalari
class LeadershipPositionAdmin(admin.ModelAdmin):
    ''' Rahbariyat lavozimlari '''
    list_display = ['name', 'short_name']
admin.site.register(LeadershipPosition, LeadershipPositionAdmin)

class LeadershipAdmin(admin.ModelAdmin):
    ''' Rahbariyat '''
    list_display = ['position', 'user', 'phone_number', 'pk']
admin.site.register(Leadership, LeadershipAdmin)




# ====================================================================
# Fakultetlarga oid sozlamalar
class PositionEmployeeFacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'id']
admin.site.register(PositionEmployeeFaculty, PositionEmployeeFacultyAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Faculty, FacultyAdmin)

class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ['user','faculty', 'position', 'phone_number', 'id']
admin.site.register(FacultyMember, FacultyMemberAdmin)







# =======================================================================
# Kafedraga oid sozlamalar
class CafedraAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Cafedra, CafedraAdmin)

class CafedraEmployeePositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'pk']
admin.site.register(CafedraEmployeePosition, CafedraEmployeePositionAdmin)

class CafedraMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'position', 'cafedra', 'phone_number', 'description']
admin.site.register(CafedraMember, CafedraMemberAdmin)




# =====================================================================
# O'quv rejaga oid sozlamalar
class ScienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cafedra']
admin.site.register(Science, ScienceAdmin)

class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'language', 'study_form', 'code', 'year', 'study_year']
admin.site.register(Direction, DirectionAdmin)

class SemestrStudyPlanAdmin(admin.ModelAdmin):
    list_display = ['direction', 'number_semestr', 'id']
admin.site.register(SemestrStudyPlan, SemestrStudyPlanAdmin)

class ScienceStudyPlanAdmin(admin.ModelAdmin):
    list_display = ['science', 'semestr_plan', 'science_code', 'exam_type', 'credit', 'course_work']
    fieldsets = (
        (_("Fan sozlamalri"), {"fields": ("science", "science_code", "exam_type", "credit")}),
        (_('Semestr rejasi sozlamasi'), {"fields": ("semestr_plan",)}),
        (_("Vaqt sozlamalari"), {"fields": ("lecture", "practice", "seminar", "laboratory", "independent_work")}),
        (_("Kurs ishi"), {"fields": ("course_work",)}),
    )
admin.site.register(ScienceStudyPlan, ScienceStudyPlanAdmin)

class ProfessionalPracticeAdmin(admin.ModelAdmin):
    list_display = ['semestr_plan', 'time']
admin.site.register(ProfessionalPractice, ProfessionalPracticeAdmin)




















ADMIN_UNREGISTER_LIST = (
    Group, 
    LeadershipPosition,
    CafedraEmployeePosition,
    PositionEmployeeFaculty,
)

if settings.DEBUG == True:
    for _ in ADMIN_UNREGISTER_LIST:
        admin.site.unregister(_)