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
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Technology)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
    )