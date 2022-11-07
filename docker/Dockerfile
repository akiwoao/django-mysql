FROM python:3.10.7-slim-buster
ENV PYTHONUNBUFFERED 1

ARG project_dir=/project/

WORKDIR $project_dir

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev

COPY ./app/requirements.txt $project_dir

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . $project_dir
