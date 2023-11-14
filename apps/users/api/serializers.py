from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
        
class TestUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    
    def validate_username(self, value):
        print(value)
        print('Pasó validación username')
        return value
    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('El campo email no puede estar vacío')
        if self.validate_username(self.context['username']) in value:
            raise serializers.ValidationError('El email no puede contener el username')
        print('Pasó validación email')
        return value
    def validate_password(self, value):
        print(value)
        print('Pasó validación password')
        return value
    def validate(self, data):
        # if data['username'] in data['email']:
        #     raise serializers.ValidationError('El email no puede contener el username')
        print('Validaciones generales')
        return data
    
    def create(self, validated_data):
        print('Creando usuario')
        return User.objects.create(**validated_data)
