from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, LoginSerializer


# Views Criadas


@login_required
def home(request):
    template_path = 'home.html'
    print(f'Tentando renderizar: {template_path}')#log
    return render(request, template_path)

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(selfself, request):
        return render(request, 'signup.html')





class LoginView(generics.GenericAPIView):
    serializer_class =  LoginSerializer

    def get(self, request):
        #agora renderiza uma página de login ou
        return render(request, 'login.html')

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']  #email
            password = serializer.validated_data['password'] #senha

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso")
                return redirect('home') #rediciona pós login (mudar depois)
            messages.error(request, "Credenciais inválidas")
            return redirect('signup')

        return Response({"error":"Credenciais inválidas"},status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] #protege o acesso com autenticação


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] #protege o acesso com autenticação


def logoutview(request):
    logout(request) #finalizador
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('home')