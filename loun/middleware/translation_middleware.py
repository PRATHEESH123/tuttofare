import re

from django.http import HttpRequest, HttpResponse
from googletrans import Translator


class TranslationMiddleware:

    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response
        self.translator = Translator()
        self.pattern = re.compile(r': *"(?P<value>[\w\s]*)",?')
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):

        self.lang = request.GET.get('lang')

        response = self.get_response(request)

        if self.lang and self.lang != 'en':
            response_text: str = response.content.decode("utf-8")

            found = self.pattern.findall(response_text)
            for i in found:
                j = self.translate(i)
                print(i, j.text)
                response_text = response_text.replace(i, j.text)

            response.content = response_text.encode('utf-8')
        return response

    def translate(self, text):
        return self.translator.translate(text, dest=self.lang, src='en')
