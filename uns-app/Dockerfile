ARG DOCKER_IMAGE_VERSION

FROM node:${DOCKER_IMAGE_VERSION}

WORKDIR /app

COPY ./app/package.json /app

RUN npm install

COPY ./app /app

CMD npm start