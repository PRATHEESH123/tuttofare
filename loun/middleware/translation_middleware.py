import re

from functools import lru_cache

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
            content = response.content.decode("utf-8")
            content = self.pattern.sub(self.translation, content)
            response.content = content.encode('utf-8')

        return response

    @lru_cache(maxsize=None)
    def cache_translation(self, text, dest):
        """ a seprate function is used to translate the match, in order
            to have differnet cache for each of the languages
        """
        return self.translator.translate(text, dest=dest, src='en')

    def translation(self, match):
        lang = self.cache_translation(match.group('value'), self.lang)
        return ''.join((match.group('start'), lang.text, match.group('end')))
