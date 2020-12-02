
from django.http.response import HttpResponse, HttpResponseServerError
from django.http.request import HttpRequest
import time
import minify_html
import htmlmin
import sys


class CustomMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response


    def process_view(self, request, view_func, view_args, view_kwargs):
        self.ts = time.time()
        print(f" Middleware view = {view_func.__name__} ")

        ua = request.META['HTTP_USER_AGENT']
        if "Bot" in ua:
            return HttpResponseServerError("BAD USERAGENT")


        return None


    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response


    def process_response(self, request, response):

        s = response.content.decode("utf-8")
        try:
            s = minify_html.minify(s)
        except:
            s = htmlmin.minify(s, remove_comments=True, remove_all_empty_space=True)

        response.content = s
        response["Content-Length"] = len(response.content)

        duration = time.time() - self.ts
        response["X-Duration"] = duration*1000
        return response

    def process_exception(self, request : HttpRequest, exception):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = exc_tb.tb_frame.f_code.co_filename
        print("plik :",fname)
        return HttpResponseServerError("Awaria - pracujemy nad tym")