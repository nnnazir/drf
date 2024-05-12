from rest_framework.pagination import PageNumberPagination


class LessonPagination(PageNumberPagination):
    """
    Пагинатор для вывода уроков.
    Указываем:
    page_size - количество уроков на странице;
    page_size_query_param - параметр запроса для указания количества
    уроков на странице;
    max_page_size - максимальное количество уроков на странице.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
