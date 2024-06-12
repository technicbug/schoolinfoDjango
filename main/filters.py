import django_filters
from .models import Image

class ImageModelFilter(django_filters.FilterSet):
    loc_num = django_filters.CharFilter(lookup_expr='exact')  # 정확히 일치하는 문자열로 필터링

    class Meta:
        model = Image
        fields = ['loc_num']
