from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nome', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'required': True, #obrigatorio
            },
            'email': {
                'required': True, #torna o campo de email obrigatório
                'allow_blank': False, #sem campo vazio
            },
        }

    def create(self, validated_data):

        user = User(
            email=validated_data['email'].lower(),
            nome=validated_data['nome'],  # Corrigido para 'nome'
        )
        user.set_password(validated_data['password'])  # Garante que a senha seja salva de forma segura
        user.save()
        return user

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():  # Acessa valor do email
            raise serializers.ValidationError("Já existe um usuário cadastrado com esse email.")
        return value  # Retorne o valor validado
