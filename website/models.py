from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    title = models.CharField("Titre professionnel", max_length=200)
    bio = models.TextField("Biographie")
    photo = models.ImageField(upload_to="profile/")
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):

    CATEGORY_TYPE_CHOICES = [
        ("technical", "Compétence technique"),
        ("managerial", "Compétence managériale"),
    ]

    CATEGORY_CHOICES = [
        ("development", "Développement logiciel & Web"),
        ("database", "Bases de données"),
        ("architecture", "Architecture & Systèmes d'information"),
        ("project", "Gestion de projets IT"),
        ("security", "Sécurité informatique"),
        ("infrastructure", "Infrastructure & Administration IT"),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Compétence"
    )

    percentage = models.PositiveIntegerField(
        verbose_name="Niveau de maîtrise (%)"
    )

    category_type = models.CharField(
        max_length=20,
        choices=CATEGORY_TYPE_CHOICES,
        default="technical",
        verbose_name="Type de compétence"
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="development",
        verbose_name="Domaine"
    )

    icon = models.CharField(
        max_length=50,
        default="fa-code",
        verbose_name="Icône Font Awesome",
        help_text="Exemple : fa-python, fa-database, fa-shield-halved"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.name

class Service(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    short_description = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=50,
        default="fa-laptop-code",
        help_text="Nom de l'icône Font Awesome"
    )

    technologies = models.TextField(
        blank=True,
        help_text="Python, Django, MySQL..."
    )

    methodology = models.TextField(
        blank=True
    )

    examples = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

class Technology(models.Model):

    CATEGORY_CHOICES = [
        ("development", "Développement"),
        ("database", "Bases de données"),
        ("architecture", "Architecture & SI"),
        ("project", "Gestion de projets"),
        ("security", "Sécurité"),
        ("infrastructure", "Infrastructure"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Technologie"
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="development",
        verbose_name="Domaine"
    )

    icon = models.CharField(
        max_length=50,
        default="fa-code",
        verbose_name="Icône Font Awesome",
        help_text="Exemple : fa-python, fa-database, fa-github"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    technologies = models.ManyToManyField(
    Technology,
    related_name="projects",
    blank=True
    )
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    created_at = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.position


class Education(models.Model):
    school = models.CharField(max_length=200)
    diploma = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.diploma


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject