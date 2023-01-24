ARG DOCKER_IMAGE_VERSION

FROM python:${DOCKER_IMAGE_VERSION}

WORKDIR /app

COPY ./app/requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./app /app

RUN chmod +x ./start.sh

CMD ./start.sh