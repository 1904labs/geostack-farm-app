FROM python:3.8.5-alpine3.11

# Build Args
ARG BUILD_DATE=None
ARG VCS_REF=None
ARG BUILD_VERSION=None

# Labels.
LABEL maintainer="gjunge@1904labs.com" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.name="1904labs/geohack-collab-project" \
      org.label-schema.description="1904labs Geosaptial Hackathon Collaborative Project" \
      org.label-schema.url="https://1904labs.com/" \
      org.label-schema.vcs-url="https://github.com/1904labs/geohack-collab-project" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.vendor="1904labs" \
      org.label-schema.version=${BUILD_VERSION} \
      org.label-schema.docker.cmd="docker run -p 8080:80 -d 1904labs/geohack-collab-project:latest"

RUN set -ex && \
    apk add --update --no-cache bash nodejs npm &&\
    pip3 install pipenv

COPY . /opt/project
WORKDIR /opt/project

RUN pipenv install --deploy --system 
RUN npm ci 
RUN npm run build 
CMD [ "gunicorn", \
    "app:create_app('production')", \
    "--workers", "15", \
    "--bind", "0.0.0.0:8080" \
    ]
