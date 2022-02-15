from django.db.models import Q
from django_filters import ModelChoiceFilter
from django_filters import rest_framework as filters

from user.models import Role, User


class UserFilter(filters.FilterSet):
    role = ModelChoiceFilter(queryset=Role.objects.all(),
                             field_name='role', method='filter_role')

    def filter_role(self, queryset, name, value):
        return queryset.filter(roles=value)

    class Meta:
        model = User
        fields = ['role', 'is_staff', 'is_superuser', 'is_active', 'blocked',
                  'verified']
