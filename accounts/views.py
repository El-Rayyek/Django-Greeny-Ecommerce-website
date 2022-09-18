from django.shortcuts import render
from .models import Profile , UserAddress , UserPhoneNumbers
from .forms import ProfileSign
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def signup(request):
    '''
    form ---> data[submit]
    create account[not activate]
    send activation code : redirect[form activation code]
    active : redirect[profile]
    '''
    if request.method == 'POST':
        form = ProfileSign(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            send_mail(
                        'Active your Account',
                        f'This code {profile.code} for activate your account',
                        settings.EMAIL_HOST_USER,
                        [email,],
                        fail_silently=False,
                    )

    else :
        form = ProfileSign()
    return render(request,'registeration/signup.html',{'form':form})



def profile(request):
    pass

def edit_profile(request):
    pass
