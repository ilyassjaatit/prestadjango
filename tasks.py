from invoke import task


@task
def wait_for(ctx, host, timeout=30):
    ctx.run(f"wait-for-it {host} --timeout={timeout}")


@task
def runserver(ctx, host="0.0.0.0", port=8000, debug=False):
    task = "runserver"
    options = []

    if debug:
        task = "runserver_plus"
        options = ["--threaded", "--print-sql", "--nopin"]

    command = " ".join([f"python manage.py {task}", f"{' '.join(options)} {host}:{port}"])
    print(command)
    ctx.run(command, pty=True)


@task
def migrate(ctx):
    ctx.run("python manage.py migrate")


@task
def celery_queues(ctx, log_level="DEBUG"):
    command = f"celery -A config.celery worker -l {log_level} "
    print(command)
    ctx.run(command, pty=True)


@task
def celery_beat(ctx, log_level="DEBUG"):
    command = f"celery -A config.celery beat -l {log_level} "
    print(command)
    ctx.run(command, pty=True)


@task
def flower(
    ctx,
):
    command = f"celery -A config.celery flower  --broker=amqp://guest:guest@localhost:5672// "
    print(command)
    ctx.run(command, pty=True)
