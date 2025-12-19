from django.contrib import admin
from .models import Program, Course, Instructor, Project, Testimonial, Event, ContactMessage

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CourseInline]
    list_display = ('title', 'level', 'duration_weeks', 'fee', 'is_active')
    list_filter = ('level', 'is_active')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'program', 'hours')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student_name', 'created_at')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'show_on_home', 'created_at')
    list_filter = ('show_on_home',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'location', 'seats', 'is_open')
    list_filter = ('is_open', 'date')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'received_at', 'handled')
    list_filter = ('handled',)