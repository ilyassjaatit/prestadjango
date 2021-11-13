FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # wait-for-it https://github.com/vishnubob/wait-for-it
  && apt-get install --no-install-recommends -qy wait-for-it \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r  ./requirements.txt

WORKDIR /app