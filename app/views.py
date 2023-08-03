from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import os
from django.conf import settings
from .models import ContactMessage

# Create your views here.


def index(request):
    return render(request,'index.html')

def CV(request):
    cv_file_path = os.path.join(settings.BASE_DIR, 'D:\django_projects\PortfolioSite\main\ShoaibCV.pdf')

    if os.path.exists(cv_file_path):
        response = FileResponse(open(cv_file_path, 'rb'))
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename="ShoaibCV.pdf"'
        return response
    else:
        return HttpResponse("CV file not found.", status=404)
    


def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('textarea', '')

        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()
        
                


        # For simplicity, let's just return a basic HttpResponse for now:
        return HttpResponse("Form submitted successfully!")

    # If it's a GET request, render the template containing the form
    return HttpResponse('submit data')
