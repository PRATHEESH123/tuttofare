import re

from django.http import HttpRequest, HttpResponse
from googletrans import Translator


class TranslationMiddleware:

    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response
        self.translator = Translator()
        self.pattern = re.compile(r'(?P<start>: *")(?P<value>[\w\s]*)(?P<end>",?)')
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):

        self.lang = request.GET.get('lang')

        response = self.get_response(request)

        if self.lang and self.lang != 'en':
            response_text: str = response.content.decode("utf-8")

            def func(matchobj):
                lang = self.translate(matchobj.group('value'))
                return ''.join((matchobj.group('start'), lang.text, matchobj.group('end')))

            response_text = self.pattern.sub(func, response_text)

            response.content = response_text.encode('utf-8')
        return response

    def translate(self, text):
        return self.translator.translate(text, dest=self.lang, src='en')
