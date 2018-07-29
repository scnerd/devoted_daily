FROM python:3.7-alpine

RUN apk update \
#  && apk add jpeg-dev zlib-dev \
  && apk add --virtual build-deps gcc linux-headers libc-dev python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 uwsgi \
  && apk del build-deps

EXPOSE 8000
EXPOSE 3031

ADD requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
ADD . .

CMD ["./run_deployment.sh"]