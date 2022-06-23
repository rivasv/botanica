from .models import Suscripcion
from rest_framework import serializers

class SuscripcionSerializer(serializers.ModelSerializer):
    rut = serializers.CharField(required=True, min_length=3)    # validar que sean al menos 3 caracteres

    def validate_rut(self, value):
        rut = Suscripcion.objects.filter(rut=value).exists()      # valido si ya existe en la bd
        if rut:
            raise serializers.ValidationError("Suscripcion para rut ya existe")
        return value


    class Meta:
        model = Suscripcion
        fields = '__all__'

#    rut = serializers.CharField(read_only=True)

#    def validate_nombre(self, value):
#        existe = Suscripcion.objects.filter(rut=value).exists
#        if existe:
#            raise serializers.ValidationError("suscripcion para rut ya existe")
#        return value

