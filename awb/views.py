from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from form.models import ContactUs, Service, ServiceImage, INFO, GalleryImage
from django.contrib import messages as MSG
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def is_authenticated(request):
    if request.session.get('is_authenticated'):
        pass
    else:
        raise Http404


def home(request):
    info = INFO.objects.all()[0]
    context = {
        'gallery_images' : GalleryImage.objects.all().order_by('-id'),
        'info' : info,
        'services' : Service.objects.all().order_by('-id')
    }
    return render(request, 'base.html', context)



def contact_us(request):
    if request.method == 'POST':
        fname = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        message = request.POST.get('message').strip()
        if fname  and email and message:
            ContactUs.objects.create(
                fname = fname,
                email = email,
                message = message
            )
            message = render_to_string('email.html', {
                'fname' : fname,
                'email' : email,
                'message' : message
            })
            email_message = EmailMessage(subject="Email from site", body=message, from_email='hafidlazar45@gmail.com', to=["electeam.ec@gmail.com"])
            email_message.send()
            return HttpResponse()
        else:
            raise
    return redirect('home')

def admin(request):
    is_authenticated(request)
    return render(request, 'admin.html')

def login(request):
    if request.method == 'POST':
        if request.POST.get('password') == 'electeam-991$' and request.POST.get('email') == "elec@team.com":
            request.session['is_authenticated'] = True
            return redirect('admin')
    
    return render(request, 'login.html')

def profile(request):
    is_authenticated(request)
    info = INFO.objects.all()[0]
    if request.method == "POST":
        info.welcome = request.POST.get('welcome').strip()
        info.description = request.POST.get('description').strip()
        try:
            image = request.FILES.get('image')
            if image:

                image.name = 'main_image' + "." + image.name.split('.')[-1]
                info.main_image.delete()
                info.main_image = image
            video = request.FILES.get('video')
            if video:
                video.name = 'video' + "." + video.name.split('.')[-1]
                info.video .delete()
                info.video = video
            info.save()

            for image in request.FILES.getlist('gallery_images'):
                image_model = GalleryImage.objects.create()
                image.name = str(image_model.id) + "." + image.name.split('.')[-1]
                image_model.image = image
                image_model.save()

            MSG.success(request, 'Profile updated successfuly.')
        except:
            MSG.error(request, 'Profile was not updated successfuly.')
    
    context = {
        'gallery_images' : GalleryImage.objects.all().order_by('-id'),
        'info' : info,
    }
    return render(request, 'profile.html', context)

def services(request):
    is_authenticated(request)
    services = Service.objects.all().order_by('-id')
    context = {
        'services' : services
    }
    return render(request, 'services.html', context)

def add_service(request):
    is_authenticated(request)
    if request.method == 'POST':
        title = request.POST.get('title').strip()
        description = request.POST.get('description').strip()
        images = request.FILES.getlist('service_images')
        if title and description:
            try:
                service = Service.objects.create(
                    title = title,
                    paragraph = description
                )
                for image in images:
                    image_model = ServiceImage.objects.create(
                        service = service
                    )
                    image.name = str(image_model.id) + "." +image.name.split('.')[-1]
                    image_model.image = image
                    image_model.save()
                MSG.success(request, 'Service was created successfully')
                
            except:
                MSG.warning(request, 'Service was not created')
        return redirect('services')
    return render(request, 'add_service.html')

def delete_service(request):
    is_authenticated(request)
    id = int(request.GET.get('id'))
    Service.objects.get(id=id).delete()
    return HttpResponse('')

def delete_g_image(request):
    is_authenticated(request)
    id = int(request.GET.get('id'))
    GalleryImage.objects.get(id=id).delete()
    return HttpResponse('')
