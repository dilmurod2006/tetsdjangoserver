from rest_framework import serializers

from Works.models import Works, Category

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ['id','title', 'author', 'category', 'price_type','price1', 'price2', 'phone_number1', 'phone_number2', 'body', 'image']