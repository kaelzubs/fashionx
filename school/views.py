from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Program, Course, Instructor, Project, Testimonial, Event, ContactMessage

def home(request):
    programs = Program.objects.filter(is_active=True)[:6]
    projects = Project.objects.all()[:8]
    testimonials = Testimonial.objects.filter(show_on_home=True)[:6]
    events = Event.objects.filter(is_open=True).order_by('date')[:3]
    return render(request, 'school/home.html', {
        'programs': programs,
        'projects': projects,
        'testimonials': testimonials,
        'events': events,
    })

def program_list(request):
    programs = Program.objects.filter(is_active=True)
    return render(request, 'school/program_list.html', {'programs': programs})

def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug, is_active=True)
    return render(request, 'school/program_detail.html', {'program': program})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'school/course_detail.html', {'course': course})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'school/instructor_list.html', {'instructors': instructors})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'school/project_list.html', {'projects': projects})

def event_list(request):
    events = Event.objects.order_by('date')
    return render(request, 'school/event_list.html', {'events': events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'school/event_detail.html', {'event': event})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        ContactMessage.objects.create(
            name=name, email=email, phone=phone,
            subject=subject, message=message_text
        )

        send_mail(
            subject=f'New contact: {subject}',
            message=f'From: {name} <{email}>\nPhone: {phone}\n\n{message_text}',
            from_email=None,
            recipient_list=['admin@example.com'],
        )

        messages.success(request, 'Thanks for reaching out. We will get back to you soon.')
        return redirect('school:contact')

    return render(request, 'school/contact.html')