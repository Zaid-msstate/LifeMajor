from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Institution
from .models import Department
from .models import Major
from .models import Student

admin.site.register(Institution)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Student)
