from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from . import forms
from . import models
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.


def store_file(file):
    with open('temp/image.png','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model=models.UserProfile
    fields="__all__"
    success_url ="/profiles"
# class CreateProfileView(View):
#     def get(self,request):
#         form = forms.ProfileForm()
#         return render(request,'profiles/create_profile.html',{"form":form})
    
#     def post(self,request):
#         submited_form = forms.ProfileForm(request.POST,request.FILES)
#         if submited_form.is_valid():
#             #store_file(request.FILES['image'])
#             print(request.FILES['user_image'])
#             user = models.UserProfile(image=request.FILES['user_image'])
#             user.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request,'profiles/create_profile.html',{"form":submited_form})


class ProfilesView(ListView):
    model=models.UserProfile
    template_name="profiles/user_profile.html"
    context_object_name="profiles"

