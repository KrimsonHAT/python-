from rest_framework import serializers
from portfolio import models 

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description' ,
            'image',
            'link' ,
            'created', 
            'updated',
    
           
        )
        model = models.Project