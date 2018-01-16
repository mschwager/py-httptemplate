
# alpine:3.6
FROM alpine@sha256:d6bfc3baf615dc9618209a8d607ba2a8103d9c8a405b3bd8741d88b4bef36478

RUN apk add --no-cache \
    alpine-sdk \
    python3 \
    python3-dev

RUN mkdir -p \
    /var/www/root/src/

RUN python3 -m pip install pipenv

COPY src/ui_pkg/ /var/www/root/
WORKDIR /var/www/root/
RUN pipenv install --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "python3", "-m", "uitemplate"]
