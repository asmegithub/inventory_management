from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrStaff


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = CustomUserCreationForm() #no argument is needed here
        return render(request, "users/register.html", {"form": form})
class LoginView(LoginView):
    template_name="users/login.html"


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        # validation
        if serializer.validated_data['email'] == "":
            raise serializers.ValidationError("Email cannot be empty")
        if serializer.validated_data['username'] == "":
            raise serializers.ValidationError("Username cannot be empty")
        if serializer.validated_data['password'] == "":
            raise serializers.ValidationError("Password cannot be empty")
        serializer.save()
        return super().perform_create(serializer)
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(id=self.request.user.id)