from config.celery import app as celery_app


@celery_app.task()
def add(x, y):
    """
    https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
    add.delay(4, 4)
    """
    return x + y
