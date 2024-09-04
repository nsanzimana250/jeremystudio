from django.shortcuts import render
from .models import Image
from .models import Video
from .models import Customer, CustomerProduct,customer_videos
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from django.contrib import messages
from django.http import JsonResponse


from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        name = request.POST.get('form_name')
        email = request.POST.get('form_email')
        subject = request.POST.get('form_subject')
        phone_number = request.POST.get('form_phone')
        message = request.POST.get('form_message')

        # Create and save the Contact instance
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            phone_number=phone_number,
            message=message
        )
        contact.save()

        # Add a success message
        messages.success(request, 'Your message has been sent successfully.')

        # Check if the request is AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'true', 'message': 'Your message has been sent successfully.'})
        else:
            return redirect('/#contact')  # Redirect to the contact section after POST

    return render(request, 'index.html')


def image(request):
    images = Image.objects.all()  # Query all Image objects
    return render(request, 'image.html', {'images': images})
  
def video(request):
    videos = Video.objects.all()  # Query all Video objects
    return render(request, 'video.html', {'videos': videos})
  

def mycustomer(request):
    customers = Customer.objects.all()
    products = CustomerProduct.objects.all()
    return render(request, 'mycustomer.html', {'customers': customers, 'products': products})

def customervideos(request):
    customers = Customer.objects.all()
    videos = customer_videos.objects.all()
    return render(request, 'customervideos.html', {'customers': customers, 'videos': videos})


def services(request):
    return render(request, 'services.html')