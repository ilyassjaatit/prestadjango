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

