from django.contrib import admin

from .models import Contact, Teacher, Passout, Testimonial, Student10, Student12
from django.contrib.admin.sites import site

# Register your models here.
admin.site.register(Contact),
admin.site.register(Teacher)
admin.site.register(Passout)
#admin.site.register(Principal)
admin.site.register(Testimonial)
admin.site.register(Student10)
admin.site.register(Student12)


