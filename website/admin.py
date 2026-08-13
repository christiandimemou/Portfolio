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

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "category_type",
        "percentage",
        "order",
    )

    list_filter = (
        "category_type",
        "category",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "category",
        "order",
    )

    list_editable = (
        "percentage",
        "order",
    )