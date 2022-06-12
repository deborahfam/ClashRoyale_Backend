from rest_framework import serializers

def get_serializer(Model):
    class Serializer(serializers.ModelSerializer):
        class Meta:
            model=Model
            fields = '__all__'
    
    return Serializer