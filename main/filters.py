import django_filters
from .models import Image

class ImageModelFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')  # 대소문자 구분 없이 포함하는 문자열로 필터링

    class Meta:
        model = Image
        fields = ['loc_num']