from .models import RequestLog


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логика перед выполнением view
        response = self.get_response(request)
        # Логика после выполнения view
        self.log_request(request)
        return response

    def log_request(self, request):
        # Извлечение значения параметра 'text' из запроса
        text_param = request.GET.get('text', '')

        # Создание записи в базе данных
        RequestLog.objects.create(
            path=request.path,
            method=request.method,
            remote_addr=request.META.get('REMOTE_ADDR'),
            query_params=request.META.get('QUERY_STRING'),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            text_param=text_param,  # Сохранение значения параметра text
        )
