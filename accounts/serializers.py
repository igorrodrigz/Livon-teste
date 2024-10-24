from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nome', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            nome=validated_data['nome'],  # Corrigido para 'nome'
        )
        user.set_password(validated_data['password'])  # Garante que a senha seja salva de forma segura
        user.save()
        return user

    def validate_email(self, value):  # Nome corrigido
        if User.objects.filter(email=value).exists():  # Acesso ao valor do email
            raise serializers.ValidationError("Já existe um usuário cadastrado com esse email.")
        return value  # Retorne o valor validado
