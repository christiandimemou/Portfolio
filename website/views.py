from django.shortcuts import render
from .forms import ContactForm
from .models import Profile, Skill, Project, Service, Experience, Education, Technology

from django.shortcuts import get_object_or_404
    


def home(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all()

    projects = Project.objects.all()

    services = Service.objects.all()

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "services": services,
    }

    return render(request, "home.html", context)

def about(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    experiences = Experience.objects.all()

    context = {
        "profile": profile,
        "education": education,
        "experiences": experiences,
    }

    return render(request, "about.html", context)


def services(request):

    services = Service.objects.all()

    context = {
        "services": services
    }

    return render(
        request,
        "includes/services.html",
        context
    )

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug
    )

    context = {
        "service": service
    }

    return render(
        request,
        "includes/service_detail.html",
        context
    )

def skills(request):

    skills = Skill.objects.all()

    category_config = [
        {
            "slug": "development",
            "name": "Développement Logiciel & Web",
            "icon": "fa-code",
            "color": "#0d6efd",
        },
        {
            "slug": "database",
            "name": "Bases de Données",
            "icon": "fa-database",
            "color": "#20c997",
        },
        {
            "slug": "architecture",
            "name": "Architecture & Systèmes d'Information",
            "icon": "fa-sitemap",
            "color": "#ffae00",
        },
        {
            "slug": "project",
            "name": "Gestion de Projets IT",
            "icon": "fa-chart-line",
            "color": "#9747ff",
        },
        {
            "slug": "security",
            "name": "Sécurité Informatique",
            "icon": "fa-shield-halved",
            "color": "#ff334f",
        },
        {
            "slug": "infrastructure",
            "name": "Infrastructure & Administration IT",
            "icon": "fa-server",
            "color": "#00b8d9",
        },
    ]

    skill_categories = []

    radar_values = []

    for category in category_config:

        category_skills = skills.filter(
            category=category["slug"]
        )

        skill_categories.append({
            **category,
            "skills": category_skills,
        })

        if category_skills.exists():

            average = sum(
                skill.percentage
                for skill in category_skills
            ) / category_skills.count()

            radar_values.append(round(average))

        else:

            radar_values.append(0)

    context = {
        "skills": skills,

        "skill_categories": skill_categories,

        "skill_count": skills.count(),

        "project_count": Project.objects.count(),

        "category_count": len(category_config),

        "technology_count": Technology.objects.count(),

        "technologies": Technology.objects.all(),

        "radar_values": radar_values,
    }

    return render(
        request,
        "skills.html",
        context
    )


def projects(request):

    projects = Project.objects.prefetch_related(
        "technologies"
    ).all()

    categories = [
        {
            "slug": "all",
            "name": "Tous",
            "icon": "fa-grid-2",
        },
        {
            "slug": "web",
            "name": "Développement Web",
            "icon": "fa-globe",
        },
        {
            "slug": "software",
            "name": "Logiciel",
            "icon": "fa-code",
        },
        {
            "slug": "information_system",
            "name": "Systèmes d'Information",
            "icon": "fa-sitemap",
        },
        {
            "slug": "management",
            "name": "Management",
            "icon": "fa-briefcase",
        },
        {
            "slug": "data",
            "name": "Data & BD",
            "icon": "fa-database",
        },
        {
            "slug": "social",
            "name": "Innovation Sociale",
            "icon": "fa-hand-holding-heart",
        },
    ]

    featured_projects = projects.filter(
        featured=True
    )

    context = {
        "projects": projects,
        "featured_projects": featured_projects,
        "categories": categories,

        "project_count": projects.count(),

        "web_count": projects.filter(
            category="web"
        ).count(),

        "information_system_count": projects.filter(
            category="information_system"
        ).count(),

        "category_count": projects.values(
            "category"
        ).distinct().count(),
    }

    return render(
        request,
        "projects.html",
        context
    )


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                "contact.html",
                {
                    "form": ContactForm(),
                    "success": True,

                    "contact_email": "christiandimemou@gmail.com",
                    "contact_phone": "+237 680507683 / 699421701",
                    "contact_location": "Cameroun",
                    "contact_hours": "Lun - Ven : 8h00 - 18h00",
                }
            )

    else:

        form = ContactForm()

    context = {
        "form": form,

        "contact_email": "christiandimemou@gmail.com",
        "contact_phone": "+237 680507683 / 699421701",
        "contact_location": "Cameroun",
        "contact_hours": "Lun - Ven : 8h00 - 18h00",
    }

    return render(
        request,
        "contact.html",
        context
    )

def project_detail(request, slug):

    project = get_object_or_404(
        Project.objects.prefetch_related("technologies"),
        slug=slug
    )

    context = {
        "project": project,
    }

    return render(
        request,
        "project_detail.html",
        context
    )

