from django.http import HttpRequest, HttpResponse


class TranslationMiddleware:

    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):

        response = self.get_response(request)
        response_text = response.content.decode("utf-8")

        response.content = response_text.encode('utf-8')
        return response
