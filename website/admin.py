from django.contrib import admin
from .models import Technology
from .models import (
    Contact,
    Education,
    Experience,
    Profile,
    Project,
    Service,
    Skill,
)


admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Technology)