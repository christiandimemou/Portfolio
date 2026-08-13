from django.shortcuts import render
from .models import Profile, Skill, Project, Service, Experience, Education
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
    return render(
        request,
        "skills.html",
        {
            "skills": Skill.objects.all()
        }
    )


def projects(request):
    return render(
        request,
        "projects.html",
        {
            "projects": Project.objects.all()
        }
    )


def contact(request):
    return render(request, "includes/contact.html")


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    context = {
        "project": project
    }

    return render(
        request,
        "includes/project_detail.html",
        context
    )