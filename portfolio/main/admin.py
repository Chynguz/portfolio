from django.contrib import admin

from main.models import About, About_me, Messaga, Project, Skils

# Register your models here.


admin.site.register(Skils)
admin.site.register(Messaga)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(About_me)
