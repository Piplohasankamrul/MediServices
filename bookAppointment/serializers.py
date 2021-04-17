from .models import *
from rest_framework import serializers

class DoctorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200,null=True)
    d_s_title = serializers.CharField(max_length=200,null=True)
    d_s_text = serializers.CharField(max_length=200,null=True)
    d1 = serializers.CharField(max_length=200,null=True)
    m_t = serializers.TimeField(max_length=200,null=True)
    e_t = serializers.TimeField(max_length=200,null=True)
    m_l = serializers.CharField(max_length=200,null=True)
    e_l = serializers.CharField(max_length=200,null=True)
    image = serializers.ImageField(null=True,blank=True)
    d2 = serializers.CharField(max_length=200,null=True)
    d3 = serializers.CharField(max_length=200,null=True)
    d4 = serializers.CharField(max_length=200,null=True)
    d5 = serializers.CharField(max_length=200,null=True)

    def create(self, validated_data):
        return Doctor.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.d_s_title = validated_data.get('d_s_title',instance.d_s_title)
        instance.d_s_text = validated_data.get('d_s_text',instance.d_s_text)
        instance.d1 = validated_data.get('d1',instance.d1)
        instance.m_t = validated_data.get('m_t',instance.m_t)
        instance.e_t = validated_data.get('e_t',instance.e_t)
        instance.m_l = validated_data.get('m_l',instance.m_l)
        instance.e_l = validated_data.get('e_l',instance.e_l)
        instance.image = validated_data.get('image',instance.image)
        instance.d2 = validated_data.get('d2',instance.d2)
        instance.d3 = validated_data.get('d3',instance.d3)
        instance.d4 = validated_data.get('d4',instance.d4)
        instance.d5 = validated_data.get('d5',instance.d5)
        instance.save()
        return instance