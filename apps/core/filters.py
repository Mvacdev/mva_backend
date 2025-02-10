# from rest_framework.filters import OrderingFilter
#
#
# class CustomOrderFilter(OrderingFilter):
#     ordering_param = 'o'
#     allowed_custom_filters = []
#     fields_related = {}
#
#     def get_ordering(self, request, queryset, view):
#         params = request.query_params.get(self.ordering_param)
#         if params:
#             fields = [param.strip() for param in params.split(',')]
#             ordering = [f for f in fields if f.lstrip('-') in self.allowed_custom_filters]
#             if ordering:
#                 return ordering
#         return self.get_default_ordering(view)
#
#     def filter_queryset(self, request, queryset, view):
#         order_fields = []
#         ordering = self.get_ordering(request, queryset, view)
#         if ordering:
#             for field in ordering:
#                 if isinstance(self.fields_related[field.lstrip('-')], str):
#                     symbol = "-" if "-" in field else ""
#                     order_fields.append(symbol + self.fields_related[field.lstrip('-')])
#                 elif isinstance(self.fields_related[field.lstrip('-')], list):
#                     for f in self.fields_related[field.lstrip('-')]:
#                         symbol = "-" if "-" in field else ""
#                         order_fields.append(symbol + f.lstrip('-'))
#         if order_fields:
#             return queryset.order_by(*order_fields)
#         return queryset
#
#
# class StorageFilter(CustomOrderFilter):
#     allowed_custom_filters = ['id']
#     fields_related = {
#         'id': ['id'],
#         'name': ['name'],
#         # 'name': ['client', 'number'],
#         # 'ip': 'ip',
#     }
