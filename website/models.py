from django.db import models



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

    CATEGORY_CHOICES = [
        ("web", "Développement Web"),
        ("software", "Développement Logiciel"),
        ("information_system", "Systèmes d'Information"),
        ("management", "Management & Gestion"),
        ("data", "Data & Bases de Données"),
        ("social", "Innovation Sociale"),
    ]

    STATUS_CHOICES = [
        ("completed", "Terminé"),
        ("ongoing", "En cours"),
        ("planned", "À venir"),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="Nom du projet"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    image = models.ImageField(
        upload_to="projects/",
        verbose_name="Image du projet"
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        blank=True,
        verbose_name="Technologies"
    )

    github_url = models.URLField(
        blank=True,
        verbose_name="Lien GitHub"
    )

    demo_url = models.URLField(
        blank=True,
        verbose_name="Lien de démonstration"
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Date de création"
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="web",
        verbose_name="Catégorie"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ongoing",
        verbose_name="Statut"
    )

    role = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Mon rôle"
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Année du projet"
    )

    featured = models.BooleanField(
        default=False,
        verbose_name="Projet mis en avant"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    class Meta:
        ordering = ["-featured", "order", "-created_at"]
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


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

    name = models.CharField(
        max_length=150,
        verbose_name="Nom"
    )

    email = models.EmailField(
        verbose_name="Adresse e-mail"
    )

    subject = models.CharField(
        max_length=200,
        verbose_name="Sujet"
    )

    message = models.TextField(
        verbose_name="Message"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'envoi"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Message lu"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"

    def __str__(self):
        return f"{self.name} - {self.subject}"