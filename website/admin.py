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
admin.site.register(Experience)
admin.site.register(Education)
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

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "year",
        "featured",
        "order",
    )

    list_filter = (
        "category",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "technologies",
    )

    list_editable = (
        "status",
        "featured",
        "order",
    )

    ordering = (
        "-featured",
        "order",
        "-created_at",
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    ordering = (
        "-created_at",
    )