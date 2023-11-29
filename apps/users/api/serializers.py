from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        print("creando Usuario")
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        print("Usuario creado DB")
        return User

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data["password"])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "username": instance.username,
            "email": instance.email,
            "password": instance.password,
        }


class TestUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def validate_username(self, value):
        print(value)
        print("Pasó validación username")
        return value

    def validate_email(self, value):
        if value == "":
            raise serializers.ValidationError("El campo email no puede estar vacío")
        # if self.validate_username(self.context['username']) in value:
        #     raise serializers.ValidationError('El email no puede contener el username')
        print("Pasó validación email")
        return value

    def validate_password(self, value):
        print(value)
        print("Pasó validación password")
        return value

    def validate(self, data):
        # if data['username'] in data['email']:
        #     raise serializers.ValidationError('El email no puede contener el username')
        print("Validaciones generales")
        return data

    def create(self, validated_data):
        print("Creando usuario")
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("Actualizando usuario")
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance
