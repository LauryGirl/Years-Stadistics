from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationCustomSize(PageNumberPagination):
    page_size_query_param = 'size'