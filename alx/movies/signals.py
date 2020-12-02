import datetime

def log_request(sender, environ, **kwargs):
    print(f"LOG REQUEST: {datetime.datetime.now()}")


def log_endrequest(sender, **kwargs):
    print(f"LOG END REQUEST: {datetime.datetime.now()}")
