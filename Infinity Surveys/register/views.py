from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.views import generic 
from django.urls import reverse_lazy
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = UserProfileForm(response.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user 
            profile.save()
        return redirect("/login")
    else: 
        form = RegisterForm()
        profile_form = UserProfileForm() 
    context = {"form":form, "profile_form": profile_form}
    return render(response, "register/register.html", context)

def profile(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/view")
    else: 
        form = RegisterForm()
    return render(response, "profile/profile.html", {"form":form}) 

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "profile/profile.html"
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user 