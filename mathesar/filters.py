from django_property_filter import (
    PropertyFilterSet, PropertyBaseInFilter, PropertyCharFilter,
    PropertyDateTimeFromToRangeFilter, PropertyBooleanFilter
)

from mathesar.models import Schema, Table


class CharInFilter(PropertyBaseInFilter, PropertyCharFilter):
    pass


class SchemaFilter(PropertyFilterSet):
    database = CharInFilter(field_name='database', lookup_expr='in')
    name = CharInFilter(field_name='name', lookup_expr='in')

    class Meta:
        model = Schema
        fields = ['database', 'name']


class TableFilter(PropertyFilterSet):
    name = CharInFilter(field_name='name', lookup_expr='in')
    schema = CharInFilter(field_name='schema__name', lookup_expr='in')
    created = PropertyDateTimeFromToRangeFilter(field_name='created_at')
    updated = PropertyDateTimeFromToRangeFilter(field_name='updated_at')
    import_verified = PropertyBooleanFilter(field_name='import_verified')
    not_imported = PropertyBooleanFilter(lookup_expr="isnull",
                                         field_name='import_verified')

    class Meta:
        model = Table
        fields = ['name', 'schema', 'created_at', 'updated_at', 'import_verified']