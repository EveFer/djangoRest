from rest_framework import serializers
from usuarios.models import User, Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('id', 'nombre')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('num_control', 'nombre', 'apellido_pat', 'apellido_mat', 'sexo', 'fecha_nac', 'direccion','carrera')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.num_control = validated_data.get('num_control', instance.num_control)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido_pat = validated_data.get('apellido_pat', instance.code)
        instance.apellido_mat = validated_data.get('apellido_mat', instance.linenos)
        instance.sexo = validated_data.get('sexo', instance.language)
        instance.fecha_nac = validated_data.get('fecha_nac', instance.fecha_nac)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.carrera = validated_data.get('carrera', instance.carrera)
        instance.save()
        return instance