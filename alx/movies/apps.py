from django.apps import AppConfig

from django.core.signals import request_started, request_finished
from .signals import *

class MoviesConfig(AppConfig):
    name = 'movies'

    def ready(self):
        request_started.connect(log_request)
        request_finished.connect(log_endrequest)