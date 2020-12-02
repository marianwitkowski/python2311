
from celery import shared_task, Task, states
from celery.exceptions import MaxRetriesExceededError, Ignore
import time

@shared_task(bind=True)
def long_taks(self, delay):
    time.sleep(delay)

