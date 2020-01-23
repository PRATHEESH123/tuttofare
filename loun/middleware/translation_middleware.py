# Used for typing
from django.http import HttpRequest
from rest_framework.response import Response

from django.utils import translation


class TranslationMiddleware:

    def __init__(self, get_response: Response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        lang = request.GET.get('lang', 'en')
        lang = request.headers.get('lang', lang)

        translation.activate(lang)

        response = self.get_response(request)

        return response
