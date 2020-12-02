
from django.http.response import HttpResponse, HttpResponseServerError
from django.http.request import HttpRequest
import time
import minify_html
import htmlmin
import sys, traceback, json, logging
import cloudwatch


class CustomMiddleware():

    def __init__(self, get_response):
        self.logger = logging.getLogger("alx")
        fmt = logging.Formatter("%(asctime)s : %(levelname)s - %(message)s ")
        handler = cloudwatch.CloudwatchHandler("ACCESS",
                                               "SECRET_KEY",
                                               "eu-central-1", "alx", "django")
        handler.setFormatter(fmt)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

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
        err = {
            "type" : str(exception.__class__.__name__),
            "traceback" : str(traceback.format_exc()),
            "headers" : str(request.headers),
            "meta" : str(request.META)
        }
        self.logger.error(json.dumps(err))
        return HttpResponseServerError("Awaria - pracujemy nad tym")