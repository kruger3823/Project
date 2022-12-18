from django.contrib import admin

from .models import med, depinformation, tableinfo, Student, TRANSACTIONS, SEM2, SEM1, SEM3, SEM4, SEM5

# Register your models here.

admin.site.register(med)
admin.site.register(depinformation)
admin.site.register(tableinfo)
admin.site.register(Student)
admin.site.register(TRANSACTIONS)


admin.site.register(SEM1)
admin.site.register(SEM2)
admin.site.register(SEM3)
admin.site.register(SEM4)
admin.site.register(SEM5)

