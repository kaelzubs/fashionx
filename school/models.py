from django.db import models

class Program(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    cover_image = models.ImageField(upload_to='programs/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['level', 'title']

    def __str__(self):
        return self.title

class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    syllabus = models.TextField(blank=True)
    hours = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructors/', blank=True, null=True)
    specialization = models.CharField(max_length=150, blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField(blank=True)
    student_name = models.CharField(max_length=120, blank=True)
    created_at = models.DateField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    show_on_home = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.rating}/5)'

class Event(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    details = models.TextField()
    banner = models.ImageField(upload_to='events/', blank=True, null=True)
    seats = models.PositiveIntegerField(default=20)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} from {self.name}'