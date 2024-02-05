from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse


class Vregistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registrarse.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return HttpResponseRedirect(
                reverse("home")
            )  # Redirect to home or any other page
        else:
            # Handle the case where the form is not valid (e.g., re-render the form with error messages)
            return render(request, "registro/registrarse.html", {"form": form})
