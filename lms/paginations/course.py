from rest_framework.pagination import PageNumberPagination


class CoursePagination(PageNumberPagination):
    """
    Пагинатор для вывода курсов.
    Указываем:
    page_size - количество курсов на странице;
    page_size_query_param - параметр запроса для указания количества
    курсов на странице;
    max_page_size - максимальное количество курсов на странице.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
