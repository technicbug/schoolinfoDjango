from rest_framework import serializers
from .models import Image

class ImageModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # URL 반환을 위해 use_url=True 설정

    class Meta:
        model = Image
        fields = ['id', 'loc_num', 'image']
