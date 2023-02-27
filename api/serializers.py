from rest_framework import serializers
from .models import Student

#Validators
def start_with_capital(value):
    if value[0].upper()!=value[0]:
        raise serializers.ValidationError("First Letter of Name must be a capital letter")

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[start_with_capital])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # Field Level Validatiom
    # def validate_roll(self, value):
    #     if(value>100):
    #         raise serializers.ValidationError("Seat Full")
    #     return value

    def validate(self, data):
        city=data.get('city')
        if city.lower()=='bhubaneswar':
            raise serializers.ValidationError("College must be IIIT Bhubaneswar")
        return data