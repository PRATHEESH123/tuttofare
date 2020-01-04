from django.http import HttpRequest, HttpResponse
from googletrans import Translator, LANGUAGES


class TranslationMiddleware:

    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response
        self.translator = Translator()
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):

        response = self.get_response(request)
        response_text = response.content.decode("utf-8")
        # print(response_text)

        print(self.translate('hello').text)

        response.content = response_text.encode('utf-8')
        return response

    def translate(self, text):
        return self.translator.translate(text, dest='ar')
